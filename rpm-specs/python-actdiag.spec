%global srcname actdiag
%global srcdesc \
actdiag and its family generate diagram images from simply text file.\
\
Features:\
- Generates beautiful diagram images from simple text format (similar to\
  graphviz’s DOT format)\
- Layouts diagram elements automatically\
- Embeds to many documentations; Sphinx, Trac, Redmine and some wikis\
\
- Supports many types of diagrams\
  - activity diagram (with this package)\
  - block diagram (with the blockdiag package)\
  - sequence diagram (with the seqdiag package)\
  - logical network diagram (with the nwdiag package)\
\
Enjoy documentation with actdiag !

Name:           python-%{srcname}
Version:        2.0.0
Release:        3%{?dist}
Summary:        Actdiag generates activity-diagram images from text

License:        ASL 2.0
URL:            http://blockdiag.com/
Source:         %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0
BuildRequires:  python3-blockdiag-devel
%endif
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pillow}
BuildRequires:  %{py3_dist reportlab}
BuildRequires:  %{py3_dist setuptools}


%description %{srcdesc}


%package -n %{srcname}
Summary:        %{summary}
Requires:       python3-%{srcname} = %{version}-%{release}


%description -n %{srcname} %{srcdesc}


%package -n python3-%{srcname}
Summary:        Python 3 module for %{srcname}
%{?python_provide:%python_provide python3-%{srcname}}


%description -n python3-%{srcname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p1


%build
%py3_build


%install
%py3_install
install -m 0644 -D %{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


%if 0
%check
%{__python3} setup.py test
%endif


%files -n %{srcname}
%license LICENSE
%doc README.rst
%{_bindir}/%{srcname}
%{_mandir}/man1/%{srcname}.1*


%files -n python3-%{srcname}
%license LICENSE
%doc PKG-INFO README.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{srcname}*
%exclude %{python3_sitelib}/%{srcname}/tests


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Dridi Boukelmoune <dridi@fedoraproject.org> - 2.0.0-1
- Bunp version to 2.0
- Drop pep8-related uptsteam patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-17
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.4-16
- Drop pep8 dependency

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 20 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.4-14
- Move the actdiag command to its own package
- Temporarilly disable the test suite

* Tue Feb 05 2019 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.4-13
- Catch up with packaging guidelines
- In general, use recommended RPM macros
- Drop the Python 2 package
- Inline package description

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-10
- Explicit reference to /usr/bin/python2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.4-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 10 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.4-6
- Python 2 binary package renamed to python2-actdiag
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.5.4-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.4-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.4-1
- Bumped to 0.5.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Mar 04 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.1-2
- Fixed changelog format.
- Fixed man page permissions.

* Sun Mar 02 2014 Dridi Boukelmoune <dridi@fedoraproject.org> - 0.5.1-1
- Initial version.
