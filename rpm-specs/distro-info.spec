Name:    distro-info
Version: 0.18
Release: 8%{?dist}

Summary: Provides information about releases of Debian and Ubuntu
License: ISC
URL:     https://tracker.debian.org/pkg/distro-info
Source0: http://deb.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz

# Remove incompatible --install-layout=deb
Patch0:  0001-Remove-install-layout.patch
# Adapt Perl path for Fedora
Patch1:  0002-Fix-Perl-path.patch
# Do not install symlink as there is no fedora-distro-info
Patch2:  0003-Do-not-install-distro-info-symlink.patch
# Disable python2
Patch4:  0004-Disable-python2.patch

BuildRequires: distro-info-data
BuildRequires: dpkg-dev
BuildRequires: gcc
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Time::Piece)
BuildRequires: /usr/bin/python
BuildRequires: python3-devel
BuildRequires: python3-flake8
BuildRequires: python3-pylint
BuildRequires: python3-setuptools
BuildRequires: shunit2

Requires: distro-info-data

%description
Information about all releases of Debian and Ubuntu. The distro-info script
will give you the codename for e.g. the latest stable release of your
distribution. To get information about a specific distribution there are the
debian-distro-info and the ubuntu-distro-info scripts.

%package -n perl-distro-info
Summary: Perl module for distro-info

BuildArch: noarch

Requires: perl-interpreter
Requires: perl(Time::Piece)
Requires: distro-info-data

%description -n perl-distro-info
This package contains a Perl module for parsing the data in distro-info-data.

%package -n python3-distro-info
Summary: Python 3 module for distro-info

BuildArch: noarch

Requires: python3
Requires: distro-info-data

%{?python_provide:%python_provide python3-distro-info}

%description -n python3-distro-info
This package contains a Python 3 module for parsing the data in
distro-info-data.

%prep
%autosetup -n %{name}

%build
make %{?_smp_mflags}

%install
%make_install

%check
PATH="/usr/share/shunit2:${PATH}" make test || true

%files
%license debian/copyright
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/*/*

%files -n perl-distro-info
%license debian/copyright
%{perl_vendorlib}/Debian

%files -n python3-distro-info
%license debian/copyright
%{python3_sitelib}/distro_info*
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.18-8
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.18-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Michael Kuhn <suraia@fedoraproject.org> - 0.18-2
- Remove python2 package
- Fix tests

* Thu Jul 19 2018 Michael Kuhn <suraia@fedoraproject.org> - 0.18-1
- Update to 0.18
- Explicitly depend on gcc and /usr/bin/python

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.17-3
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Michael Kuhn <suraia@fedoraproject.org> - 0.17-1
- Update to 0.17

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Petr Pisar <ppisar@redhat.com> - 0.14-8
- perl dependency renamed to perl-interpreter
  <https://fedoraproject.org/wiki/Changes/perl_Package_to_Install_Core_Modules>

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.14-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 04 2016 Michael Kuhn <suraia@fedoraproject.org> - 0.14-3
- Explicitly require python2.
- Rename python-* packages to python2-*.
- Provide python-distro-info.

* Tue Dec 29 2015 Michael Kuhn <suraia@fedoraproject.org> - 0.14-2
- Add license text.
- Own perl directory.
- Do not install distro-info symlink.

* Fri Nov 06 2015 Michael Kuhn <suraia@fedoraproject.org> - 0.14-1
- Initial package.
