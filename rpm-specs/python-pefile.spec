Name:           python-pefile
Version:        2019.4.18
Release:        4%{?dist}
Summary:        Python module for working with Portable Executable files
License:        MIT
URL:            https://github.com/erocarrera/pefile


%global srcname pefile

%global common_desc pefile is a multi-platform Python module to read and work with Portable\
Executable (aka PE) files. Most of the information in the PE Header is \
accessible, as well as all the sections, section's information and data.\
pefile requires some basic understanding of the layout of a PE file. Armed \
with it it's possible to explore nearly every single feature of the file.\
Some of the tasks that pefile makes possible are:\
* Modifying and writing back to the PE image\
* Header Inspection\
* Sections analysis\
* Retrieving data\
* Warnings for suspicious and malformed values\
* Packer detection with PEiD’s signatures\
* PEiD signature generation\


#Source0:        https://github.com/erocarrera/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz 
Source0:        https://github.com/erocarrera/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# For the patch
# BuildRequires: git-core 

%description
%{common_desc}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:   python3-future

%description -n python3-%{srcname}
%{common_desc}


%prep
%autosetup -n %{srcname}-%{version}
sed -i -e '/^#!\//, 1d' pefile.py

%build
%py3_build

%install
%py3_install

# check
# regression tests in this package are based on binary blob of exe files - commercial and malware
# at this point (2019-09-20) not suitable to be in Fedora.
# More info on:
# https://github.com/erocarrera/pefile/issues/171
# https://github.com/erocarrera/pefile/issues/82#issuecomment-192018385
# %{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README*
%{python3_sitelib}/*

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.4.18-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.4.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 20 2019 Michal Ambroz <rebus _AT seznam.cz> - 2019.4.18-1
- bump to version 2019.4.18

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2017.11.5-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2017.11.5-5
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2017.11.5-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 08 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2017.11.5-1
- Update to 2017.11.5 (rhbz #1509751)

* Sat Aug 05 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2017.8.1-1
- Update to 2017.8.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.5.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2017.5.26-2
- Fix requirement (rhbz #1474447)

* Sat May 27 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 2017.5.26-1
- Update to 2017.5.26
- Remove upstreamed patch

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.3.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.3.28-2
- Rebuild for Python 3.6

* Tue Nov 01 2016 Athmane Madjoudj <athmane@fedoraproject.org> - 2016.3.28-1
- Update to 2016.3.28
- Revamp the specfile
- Add patch to fix the build

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10_139-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_139-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 07 2014 Christopher Meng <rpm@cicku.me> - 1.2.10_139-1
- Update to 1.2.10_139

* Thu Aug 08 2013 Christopher Meng <rpm@cicku.me> - 1.2.10_123-1
- Update to 1.2.10_123

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.2.10_63-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.10_63-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  8 2009 David Malcolm <dmalcolm@redhat.com> - 1.2.10_63-1
- initial packaging

