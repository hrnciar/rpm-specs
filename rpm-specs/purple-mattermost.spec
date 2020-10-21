# purple-mattermost upstream hasn't released for a while,
# it was requested that we update to a snapshot:
# https://bugzilla.redhat.com/show_bug.cgi?id=1725804

%global commit e21f18c4d868bf6db4e3d436eddcaca5da5effe0
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           purple-mattermost
Version:        1.2
Release:        8.20190826gite21f18c%{?dist}
Summary:        Pidgin protocol plugin to connect to Mattermost

License:        GPLv3+
URL:            https://github.com/EionRobb/purple-mattermost

Source0:        https://github.com/EionRobb/purple-mattermost/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildRequires:  json-glib-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  libpurple-devel
BuildRequires:  gcc-c++, gcc

%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It connects libpurple-based instant messaging clients with Mattermost server.

This package provides the protocol plugin for libpurple clients.

%package -n pidgin-mattermost

Summary:        Libpurple protocol plugin to connect to Mattermost
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description -n pidgin-mattermost
A third-party plugin for the Pidgin multi-protocol instant messenger.
It connects libpurple-based instant messaging clients with Mattermost server.

This package provides the icon set for Pidgin.

%prep
%autosetup -n %{name}-%{commit}

# Allow build flag injection.
sed 's/CFLAGS	?=/CFLAGS	+=/g' -i Makefile
sed 's/LDFLAGS ?=/LDFLAGS +=/g' -i Makefile

%build
CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}" %make_build

%install
%make_install

%files
%license LICENSE
%doc INSTALL.md README.md VERIFICATION.md
%{_libdir}/purple-*/libmattermost.so

%files -n pidgin-mattermost
%{_datadir}/pixmaps/pidgin/protocols/*/mattermost.png

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8.20190826gite21f18c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7.20190826gite21f18c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.2-6.20190826gite21f18c
- Update to latest upstream git commit.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.2-3
- Rebuild with fixed binutils

* Fri Jul 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2-2
- Rebuild for new binutils

* Thu Jul 26 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.2-1
- Updated to latest upstream release.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6.20170805git4524538
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5.20170805git4524538
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-4.20170805git4524538
- License is actually GPLv3+, not GPLv3, fix tag.
- Simplify github sourceurls.

* Thu Aug 10 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-3.20170805git4524538
- Updated to a recent git snapshot in order to support gitlab workaround.

* Thu Aug 10 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.1-2
- Adapted packaging, made Fedora-compliant.

* Wed May 31 2017 Jaroslaw Polok <jaroslaw.polok@gmail.com> - 1.1-1
- Initial packaging.

