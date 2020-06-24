%define		realname PyICU
Name:		pyicu
Version:	2.5
Release:	1%{?dist}
Summary:	Python extension wrapping IBM's ICU C++ libraries

License:	MIT
URL:		https://pypi.org/project/PyICU/
Source0:	https://files.pythonhosted.org/packages/source/P/%{realname}/%{realname}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	libicu-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools
BuildRequires:	python3-six

%global _description\
PyICU is Python extension wrapping IBM's International Components\
for Unicode C++ library (ICU). ICU is a mature, widely used set of\
C/C++ and Java libraries providing Unicode and Globalization support\
for software applications. ICU is widely portable and gives applications\
the same results on all platforms and between C/C++ and Javasoftware.

%description %_description

%package -n python3-pyicu
Summary: Python 3 extension wrapping IBM's ICU C++ libraries

%description -n python3-pyicu %_description

%prep
%setup -q -n %{realname}-%{version}

%build
%py3_build

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

%install
%py3_install

# Remove tests
rm -rf %{buildroot}%{python3_sitearch}/tests

%check
%{__python3} setup.py test

%files -n python3-pyicu
%doc LICENSE
%{python3_sitearch}/PyICU*
%{python3_sitearch}/__pycache__/PyICU*
%{python3_sitearch}/icu/
%{python3_sitearch}/_icu*

%changelog
* Mon Jun 08 2020 Pete Walter <pwalter@fedoraproject.org> - 2.5-1
- Update to 2.5
- Update URL

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-3
- Rebuilt for Python 3.9

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 2.4.3-2
- Rebuild for ICU 67

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Pete Walter <pwalter@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 2.3.1-1
- Update to 2.3.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Miro Hrončok <mhroncok@redhat.com> - 2.2-2
- Subpackage python2-pyicu has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Wed Jan 23 2019 Pete Walter <pwalter@fedoraproject.org> - 2.2-1
- Update to 2.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.3-1
- Update to 2.0.3

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.2-5
- Rebuild for ICU 62

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuilt for Python 3.7

* Mon Apr 30 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.2-3
- Rebuild for ICU 61.1

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0.2-1
- Update to 2.0.2

* Tue Jan 09 2018 Pete Walter <pwalter@fedoraproject.org> - 2.0-1
- Update to 2.0

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.9.8-1
- Update to 1.9.8

* Thu Nov 30 2017 Pete Walter <pwalter@fedoraproject.org> - 1.5-25
- Rebuild for ICU 60.1

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-24
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.5-23
- Python 2 binary package renamed to python2-pyicu
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.5-20
- Rebuild due to bug in RPM (RHBZ #1468476)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5-18
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 1.5-16
- rebuild for ICU 57.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Oct 29 2015 Eike Rathke <erack@redhat.com> - 1.5-13
- fix build with ICU 56.1

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 1.5-12
- rebuild for ICU 56.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5-10
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 1.5-9
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 1.5-8
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 16 2014 Bastien Nocera <bnocera@redhat.com> 1.5-6
- Build Python3 version as well (#917449)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 Parag Nemade <paragn AT fedoraproject DOT org> - 1.5-4
- Rebuild for icu 52

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 22 2013 David Tardon <dtardon@redhat.com> - 1.5-2
- rebuild for ICU ABI break

* Fri Feb 08 2013 Jon Ciesla <limburgher@gmail.com> - 1.5-1
- libicu rebuild.
- Update to 1.5, 1.4 doesn't build on new libicu.

* Wed Aug 22 2012 Tom Callaway <spot@fedoraproject.org> - 1.4-1
- update to 1.4

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 1.2-1
- New upstream 1.2 release

* Sun May 08 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 1.1-2
- added CHANGES CREDITS under doc section
- updated URL
- added check section

* Thu Mar 17 2011 Prabin Kumar Datta <prabindatta@fedoraproject.org> - 1.1-1
- Initial build
