%global desc \
This application is able to download trailers from apple.com/trailers\
to your computer.\
It shows descriptions, posters, and other movie information.

Name:           pyqtrailer
Version:        0.6.2
Release:        25%{?dist}
Summary:        PyQt4 application to download trailers from apple.com
License:        GPLv3
URL:            http://github.com/sochotnicky/%{name}
Source0:        http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
Patch0:         0001-Improved-Py3-compatibility.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytrailer
BuildRequires:  python3-dateutil
BuildRequires:  python3-PyQt4-devel
BuildRequires:  /usr/bin/lconvert

BuildRequires:  desktop-file-utils

%description
%{desc}

%package -n python3-%{name}
Summary:        %{summary}
Requires:       python3-dateutil
Requires:       python3-pytrailer >= 0.6.0
Requires:       python3-PyQt4
Requires:       python3-future
Conflicts:      python2-%{name} < 0.6.2-18
Provides:       %{name} = %{version}-%{release}

%description -n python3-%{name}
%{desc}

%prep
%autosetup -p1

%build
%py3_build

%install
%py3_install

desktop-file-install \
    --dir=%{buildroot}%{_datadir}/applications \
     xdg/%{name}.desktop

install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 xdg/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%files -n python3-%{name}
%doc README ChangeLog
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/*.egg-info
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-24
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-22
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-21
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-18
- Subpackage python2-pyqtrailer has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Lumir Balhar <lbalhar@redhat.com> - 0.6.2-14
- Python2/3 subpackages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.6.2-11
- Fix pytrailer dependency

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.2-1
- Updated to latest upstream with updated translations
- Upstream fixed race condition during build

* Tue Feb  1 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.1-2
- Fix various build problems

* Mon Jan 31 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.1-1
- Update to latest upstream version

* Mon Nov 29 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.6.0-1
- Update to latest upstream version

* Tue Oct 26 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4.1-1
- Updated to latest upstream
- Using icon and desktop file from upstream
- Added desktop-file-utils to BR

* Mon Oct 18 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.6-2
- Added desktop entry and icon

* Fri Oct 15 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.3.6-1
- Initial version of package
