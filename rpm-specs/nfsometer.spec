Name: nfsometer		
Version: 1.9
Release: 9%{?dist}
Summary: NFS Performance Framework Tool

License: GPLv2+ 
URL: http://wiki.linux-nfs.org/wiki/index.php/NFSometer
Source0: http://www.linux-nfs.org/~dros/nfsometer/releases/%{name}-%{version}.tar.gz 
Patch001: nfsometer_py3.patch

BuildArch: noarch
BuildRequires: python3-setuptools
BuildRequires: python3-numpy
BuildRequires: python3-matplotlib
BuildRequires: python3-mako
BuildRequires: python3-devel
Requires: nfs-utils 
Requires: python3-matplotlib
Requires: python3-numpy
Requires: python3-mako
Requires: filebench
Requires: time
Requires: git

%description
NFSometer is a performance measurement framework for running workloads and 
reporting results across NFS protocol versions, NFS options and Linux 
NFS client implementations. 

%prep
%setup -q
%patch001 -p1

%build
python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/*/*
#For noarch packages: sitelib
%{python3_sitelib}/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9-8
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.9-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 23 2019 Alice Mitchell <ajmitchell@redhat.com> - 1.9-3
- Update to python3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 25 2018 Steve Dickson <steved@redhat.com> 1.9-0
- Updated to latest upstream release: 1.9

* Tue Feb 20 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.8-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.8-3
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Mar  7 2016 Steve Dickson <steved@RedHat.com> 1.8-1
- Updated to latest upstream release: 1.8

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 29 2014 Steve Dickson <steved@RedHat.com> 1.7-1
- Updated to 1.7

* Fri Nov  8 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.6-1
- Update to 1.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Weston Andros Adamson <dros@netapp.com> 1.5-1
- Updated to the latest upstream release: 1.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 Steve Dickson <steved@redhat.com> 1.3-1
- Updated to the latest upstream release: 1.3

* Wed Sep 26 2012 Steve Dickson <steved@redhat.com> 1.1-2
- Added the time and git Requires (bz 852859)

* Mon Jul 30 2012 Steve Dickson <steved@redhat.com> 1.1-1
- Incorporated review comments.

* Thu Jul 19 2012 Steve Dickson <steved@redhat.com> 1.1-0
- Inital commit.
