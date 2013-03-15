Summary:	Simple password store
Name:		password-store
Version:	1.4.2
Release:	0.1
License:	GPL v2+
Group:		Applications
Source0:	http://git.zx2c4.com/password-store/snapshot/%{name}-%{version}.tar.xz
# Source0-md5:	c6382dbf5be4036021bf1ce61254b04b
URL:		http://zx2c4.com/projects/password-store/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	bash
Requires:	gnupg2
Requires:	tree
Requires:	util-linux
Suggests:	coreutils
Suggests:	git-core
Suggests:	xclip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define zshdir %{_datadir}/zsh/site-functions
%define bashdir	%{_sysconfdir}/bash_completion.d

%description
This is a very simple password store that encrypts passwords using gpg
and places the encrypted password in a directory. It can generate new
passwords and keep track of old ones.

%package -n zsh-completion-password-store
Summary:	zsh-completion for password-store
Summary(pl.UTF-8):	Uzupełnianie nazw w zsh dla password-store
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}

%description -n zsh-completion-password-store
zsh-completion for password-store.

%description -n zsh-completion-password-store -l pl.UTF-8
Pakiet ten dostarcza funkcje uzupełniania nazw powłoki zsh dla
password-store.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zshdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir} \
	SYSCONFDIR=%{_sysconfdir}

install -m644 contrib/pass.zsh-completion $RPM_BUILD_ROOT%{zshdir}/_pass

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{bashdir}/password-store
%{_mandir}/man1/pass.1*

%files -n zsh-completion-password-store
%defattr(644,root,root,755)
%{zshdir}/_pass
