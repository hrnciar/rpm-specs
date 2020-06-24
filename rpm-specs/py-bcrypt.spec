Summary:	Python bindings for OpenBSD's Blowfish password hashing code
Name:		py-bcrypt
Version:	0.4
Release:	26%{?dist}
License:	BSD with advertising
URL:		http://code.google.com/p/py-bcrypt/
Source:		http://py-bcrypt.googlecode.com/files/py-bcrypt-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gcc

%global _description\
python-bcrypt is a Python wrapper of OpenBSD's Blowfish password hashing\
code, as described in "A Future-Adaptable Password Scheme" by Niels\
Provos and David Mazières.\
\
This system hashes passwords using a version of Bruce Schneier's Blowfish\
block cipher with modifications designed to raise the cost of off-line\
password cracking and frustrate fast hardware implementation. The\
computation cost of the algorithm is parametised, so it can be increased\
as computers get faster. The intent is to make a compromise of a password\
database less likely to result in an attacker gaining knowledge of the\
plain-text passwords (e.g. using John the Ripper).

%description %_description

%package -n python3-py-bcrypt
Summary:	Python 3 bindings for OpenBSD's Blowfish password hashing code

%description -n python3-py-bcrypt
python-bcrypt is a Python wrapper of OpenBSD's Blowfish password hashing
code, as described in "A Future-Adaptable Password Scheme" by Niels
Provos and David Mazières.

This system hashes passwords using a version of Bruce Schneier's Blowfish
block cipher with modifications designed to raise the cost of off-line
password cracking and frustrate fast hardware implementation. The
computation cost of the algorithm is parametised, so it can be increased
as computers get faster. The intent is to make a compromise of a password
database less likely to result in an attacker gaining knowledge of the
plaintext passwords (e.g. using John the Ripper). 

This package allows for use of py-bcrypt with Python 3.


%prep
%setup -q -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-py-bcrypt
%doc LICENSE README TODO
%{python3_sitearch}/py_bcrypt-%{version}-py3.*
%{python3_sitearch}/bcrypt

%changelog
* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.4-26
- BR python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4-25
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-23
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4-22
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.4-19
- Drop Python 2 per BZ 1627390.

* Fri Jul 20 2018 Kevin Fenzi <kevin@scrye.com> - 0.4-18
- Fix FTBFS bug #1605532

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4-16
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4-14
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.4-13
- Python 2 binary package renamed to python2-py-bcrypt
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4-9
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Nov 19 2013 Jon Ciesla <limburgher@gmail.com> - 0.4-1
- Latest upstream, added support for Python 3 and two new functions: bcrypt.checkpw() and bcrypt.kdf()

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jon Ciesla <limburgher@gmail.com> - 0.3-1
- Latest upstream, fixes CVE-2013-1895: concurrency issue leading to auth bypass

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 17 2010 david.r@ultracar.co.uk - 0.2-4
- Altered spec file to allow building across py2.6 and py2.7

* Thu Aug 12 2010 dcr226@fedorapeople.org - 0.2-3
- Rebuilt for python 2.7

* Wed Aug 11 2010 dcr226@fedoraproject.org - 0.2-2
- packaged for Fedora

*Mon Jun 14 2010 djm@mindrot.org
- (djm) Prefer setuptools for packaging. Based on patch from Niall
   O'Higgins.
- (djm) Release py-bcrypt-0.2

*Thu Oct 01 2009 djm@mindrot.org
- (djm) Allow Python threads to run during (potentially lengthy) bcrypt
   operation. Patch from vijay AT meebo-inc.com

*Tue Aug 08 2006 djm@mindrot.org
- (djm) Add support for Win32

*Mon May 22 2006 djm@mindrot.org
- (djm) Start
