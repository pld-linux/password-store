Summary:	Simple password store
Name:		password-store
Version:	1.6.5
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://git.zx2c4.com/password-store/snapshot/%{name}-%{version}.tar.xz
# Source0-md5:	2c4468360c678184051e76f03c2f6b04
URL:		https://www.passwordstore.org/
BuildRequires:	rpmbuild(macros) >= 1.720
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	bash
Requires:	gnupg2
Requires:	tree
Requires:	util-linux
Suggests:	coreutils
Suggests:	git-core
Suggests:	xclip
Provides:	pass = %{version}-%{release}
Obsoletes:	pass
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple password store that encrypts passwords using gpg
and places the encrypted password in a directory. It can generate new
passwords and keep track of old ones.

%package -n bash-completion-password-store
Summary:	bash-completion for password-store
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla password-store
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-password-store
bash-completion for password-store.

%description -n bash-completion-password-store -l pl.UTF-8
Pakiet ten dostarcza bashowe uzupełnianie nazw dla password-store.

%package -n fish-completion-password-store
Summary:	fish-completion for password-store
Summary(pl.UTF-8):	Uzupełnianie nazw w fish dla password-store
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	fish

%description -n fish-completion-password-store
fish-completion for password-store.

%description -n fish-completion-password-store -l pl.UTF-8
Pakiet ten dostarcza uzupełnianie nazw w fish dla password-store.

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
%{__make} install \
	BINDIR=%{_bindir} \
	LIBDIR=%{_libdir} \
	MANDIR=%{_mandir} \
	SYSCONFDIR=%{_sysconfdir} \
	FORCE_ALL=1 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pass
%{_mandir}/man1/pass.1*

%files -n bash-completion-password-store
%defattr(644,root,root,755)
%{bash_compdir}/pass

%files -n fish-completion-password-store
%defattr(644,root,root,755)
%{fish_compdir}/pass.fish

%files -n zsh-completion-password-store
%defattr(644,root,root,755)
%{zsh_compdir}/_pass
