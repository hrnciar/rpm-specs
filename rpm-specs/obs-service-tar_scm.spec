%define service tar_scm

Name:           obs-service-%{service}
Version:        0.10.10
Release:        4%{?dist}
Summary:        An OBS source service: checkout or update a tarball from svn/git/hg
License:        GPLv2+
URL:            https://github.com/openSUSE/%{name}
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  glibc-langpack-en
BuildRequires:  python3-mock
BuildRequires:  python3-six
BuildRequires:  bzr
BuildRequires:  git-core
BuildRequires:  mercurial
BuildRequires:  subversion

BuildRequires:  python3-PyYAML
BuildRequires:  python3-dateutil
BuildRequires:  python3-lxml

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       obs-service-obs_scm-common = %{version}-%{release}

BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

%package -n     obs-service-obs_scm-common
Summary:        Common parts of SCM handling services
Requires:       (glibc-langpack-en or glibc-all-langpacks)
Requires:       python3-PyYAML
Requires:       python3-dateutil
Requires:       git-core
Requires:       obs-service-download_files
Recommends:     bzr
Recommends:     mercurial
Recommends:     subversion


%description -n obs-service-obs_scm-common
This is a source service for openSUSE Build Service.

It supports downloading from svn, git, hg and bzr repositories.

This package holds the shared files for different services.

%package -n     obs-service-tar
Summary:        Creates a tar archive from local directory
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-tar
Creates a tar archive from local directory

%package -n     obs-service-obs_scm
Summary:        Creates a OBS cpio from a remote SCM resource
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-obs_scm
Creates a OBS cpio from a remote SCM resource.

This can be used to work directly in local git checkout and can be packaged
into a tar ball during build time.

%package -n     obs-service-appimage
Summary:        Handles source downloads defined in appimage.yml files
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-appimage
Experimental appimage support: This parses appimage.yml files for SCM
resources and packages them.

%package -n     obs-service-snapcraft
Summary:        Handles source downloads defined in snapcraft.yaml files
Requires:       obs-service-obs_scm-common = %{version}-%{release}

%description -n obs-service-snapcraft
Experimental snapcraft support: This parses snapcraft.yaml files for SCM
resources and packages them.


%prep
%autosetup -p1

%build
# Nothing to build

%install
%make_install PREFIX="%{_prefix}" SYSCFG="%{_sysconfdir}" PYTHON="%{__python3}"
%py_byte_compile %{__python3} %{buildroot}%{_prefix}/lib/obs/service/TarSCM

%check
# No need to run PEP8 tests here; that would require a potentially
# brittle BuildRequires: python3-pep8, and any style issues are already
# caught by Travis CI.
make test3

%files
%{_prefix}/lib/obs/service/tar_scm.service

%files -n obs-service-obs_scm-common
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-tar_scm/issues/257
%license debian/copyright
%doc README.md
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/TarSCM
%{_prefix}/lib/obs/service/tar_scm
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*

%files -n obs-service-tar
%{_prefix}/lib/obs/service/tar
%{_prefix}/lib/obs/service/tar.service

%files -n obs-service-obs_scm
%{_prefix}/lib/obs/service/obs_scm
%{_prefix}/lib/obs/service/obs_scm.service

%files -n obs-service-appimage
%{_prefix}/lib/obs/service/appimage*

%files -n obs-service-snapcraft
%{_prefix}/lib/obs/service/snapcraft*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.10-3
- Remove dependency on unittest2 (#1789200)

* Tue Dec 31 2019 Neal Gompa <ngompa13@gmail.com> - 0.10.10-2
- Rebuild to deal with random Koji+Bodhi breakage

* Fri Dec 27 2019 Neal Gompa <ngompa13@gmail.com> - 0.10.10-1
- Initial packaging
