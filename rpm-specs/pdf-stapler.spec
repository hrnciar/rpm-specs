# spec file for package pdf-stapler
#
%global commit 875325103234b4a3ed96a4a5167ff78c291edbff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20191215

Name:           pdf-stapler
Version:        1.0.0
Release:        0.6.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Tool for manipulating PDF documents from the command line
License:        BSD
URL:            https://github.com/hellerbarde/stapler
Source0:        https://github.com/hellerbarde/stapler/archive/stapler-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-more-itertools
Requires:       python3-staplelib = %{version}-%{release}

%description
pdf-stapler is the Fedora package for stapler, the opensource python
project which provides a commandline tool that staples, deletes,
concatenates and shuffles documents in the Portable Document Format
(PDF). It is an alternative to PDFtk.

From the project git page:

Philip Stark found pypdf, a PDF library written in pure Python. He
couldn't find a tool which actually used the library, so he started 
writing his own.

This version of stapler is Fred Wenzel's fork of the project, with
a completely refactored source code, tests, and added functionality.

%package -n python3-staplelib
Summary:        Module staplelib of pdf-stapler
Requires:       python3-PyPDF2
%{?python_provide:%python_provide python3-staplelib}

%description -n python3-staplelib
%{summary}.

%prep
%setup -q -n  stapler-%{commit}
sed -i 's|"PyPDF2>=1.24"||' setup.py
# Remove upper limit from more-itertools
# https://github.com/hellerbarde/stapler/issues/71
sed -i 's|"more-itertools>=2.2,<6.0.0"|"more-itertools>=2.2"|' setup.py

%build
%py3_build 

#%check
#%{__python3} setup.py test

%install
%{py3_install}

#mv $RPM_BUILD_ROOT/%{_bindir}/stapler-%{commit} $RPM_BUILD_ROOT/%{_bindir}/%{name}
rm %{buildroot}%{_bindir}/stapler
# Fedora already has a stapler package so this "stapler" package is renamed
# pdf-stapler

%files
%{_bindir}/%{name}
%doc README.rst
%license LICENSE

%files -n python3-staplelib
%{python3_sitelib}/stapler-%{version}*.egg-info
%{python3_sitelib}/staplelib/
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6.20191215git8753251
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.5.20191215git8753251
- Rebuilt for Python 3.9

* Sat Mar 21 2020 Lumír Balhar <lbalhar@redhat.com> - 1.0.0-0.4.20191215git8753251
- Remove upper limit from more-itertools dependency
Fixes: rhbz#1812845

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.3.20191215git8753251
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 28 2019 aarem AT fedoraproject DOT org - 1.0.0-1
- Minor updates to specfile 
* Thu Dec 26 2019 aarem AT fedoraproject DOT org - 1.0.0-1
- Rebuilt for python3


* Thu Dec 26 2019 aarem AT fedoraproject DOT org - 1.0.0-1
- Rebuilt for python3, added PKG-INFO.

* Mon Mar 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.3-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 05 2016 aarem AT fedoraproject DOT org - 0.3.3-8
- applied patch supplied by Raphael Groner

* Fri Jun 03 2016 Raphael Groner <projects.rg@smart.ms> - 0.3.3-7
- split module into subpackage, rhbz#1337605

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Dec 20 2015 aarem AT fedoraproject DOT org - 0.3.3-5
- made changes as per Zbigniew Jędrzejewski-Szmek
1. corrected macro signs in changelog to represent that these are comments.
2. Provided explicit Provides: in packaging

* Sun Dec 20 2015 aarem AT fedoraproject DOT org - 0.3.3-4
- made changes as per Zbigniew Jędrzejewski-Szmek
  1. changed build and install statements
  2. reduced description

* Mon Dec 14 2015 aarem AT fedoraproject DOT org - 0.3.3-3
- made changes to packaging as per Parag AN:
  1. changed %%{__python} to  %%{__python_macros}
  2. increased release number
  3. reduced changelog entry to be less than 80 characters per line
  4. added comment on why pdf-stapler is not named stapler

* Fri Dec 11 2015 aarem AT fedoraproject DOT org - 0.3.3-2
- initial repackaging to include README, and PKG-INFO in documentation

* Thu Sep 24 2015 aarem AT fedoraproject DOT org - 0.3.3-1
- initial packaging of 0.3.3 version



