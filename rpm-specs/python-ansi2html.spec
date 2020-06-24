%global srcname ansi2html

Name:       python-ansi2html
Version:    1.5.1
Release:    9%{?dist}
Summary:    Python module that converts text with ANSI color to HTML

License:    GPLv3+
URL:        http://github.com/ralphbean/ansi2html
Source0:    https://pypi.io/packages/source/a/ansi2html/ansi2html-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose
BuildRequires:  python3-mock
BuildRequires:  python3-six

%global _description\
The ansi2html module can convert text with ANSI color codes to HTML.

%description %_description

%package -n python3-ansi2html
Summary:    %summary
%{?python_provide:%python_provide python3-ansi2html}

Requires:   python3
Requires:   python3-setuptools
Requires:   python3-six

%description -n python3-ansi2html %_description

%prep
%setup -q -n %{srcname}-%{version}

# Remove bundled egg-info just in case it is included.
rm -rf *.egg*

%build
%py3_build

%install
mkdir -p %{buildroot}%{_mandir}/man1/
mv man/ansi2html.1 %{buildroot}%{_mandir}/man1/ansi2html.1
%py3_install

%check
PYTHONPATH=. nosetests-%{python3_version} tests/*.py

%files -n python3-ansi2html
%doc LICENSE README.rst
%{python3_sitelib}/ansi2html
%{python3_sitelib}/ansi2html-%{version}-*
%{_bindir}/ansi2html
%{_mandir}/man1/ansi2html.1.gz

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.1-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 02 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-3
- Bump version to pick up gating.yaml file.

* Fri Nov 02 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-2
- Bump version to pick up gating.yaml file.

* Fri Oct 19 2018 Ralph Bean <rbean@redhat.com> - 1.5.1-1
- New version
- Dropped python2 subpackage and modernized macros.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Ralph Bean <rbean@redhat.com> - 1.2.0-5
- Bump to try and trigger automated tests.

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.0-3
- Python 2 binary package renamed to python2-ansi2html
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Ralph Bean <rbean@redhat.com> - 1.2.0-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 02 2016 Ralph Bean <rbean@redhat.com> - 1.1.1-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 30 2015 Ralph Bean <rbean@redhat.com> - 1.1.0-1
- new version

* Wed Jan 28 2015 Ralph Bean <rbean@redhat.com> - 1.0.6-6
- Bump spec for testing.

* Mon Oct 13 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-5
- Modernized python2 macros.
- Remove any bundled egg-info.
- BR on python2-devel.

* Wed Aug 27 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-4
- Added explicit dependency on python(3)-setuptools.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 1.0.6-1
- Latest upstream.

* Sat Oct 12 2013 Ralph Bean <rbean@redhat.com> - 1.0.5-1
- Latest upstream with configurable color scheme.

* Sat Oct 12 2013 Ralph Bean <rbean@redhat.com> - 1.0.3-1
- Latest upstream with a tweak to setup.py

* Fri Oct 04 2013 Ralph Bean <rbean@redhat.com> - 1.0.2-1
- Latest upstream.
- Manpages now included.

* Thu Sep 26 2013 Ralph Bean <rbean@redhat.com> - 0.10.0-3
- Latest upstream with a superior internal state model thanks to Sebastian
  Pipping.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Ralph Bean <rbean@redhat.com> - 0.9.4-2
- Removed python3 rhel conditional.

* Mon Feb 25 2013 Ralph Bean <rbean@redhat.com> - 0.9.4-1
- Latest upstream fixes encoding issues.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.2-1
- New upstream
- Fixes dict ordering issues.
- Solves some encoding issues.

* Mon Aug  6 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.1-8
- fix dict ordering issues

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.9.1-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-5
- Re-enabled tests.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-4
- Temporarily removed both sets of tests until python-mock problems are sorted
  out.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-3
- Temporarily removed python3 tests until python3-mock is available.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-2
- Added requirements python-mock and python-ordereddict.
* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.1-1
- Latest upstream version.
* Tue Jun 26 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-4
- Only Require python3 for python3-ansi2html.
* Wed May 23 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-3
- Fix executable python2/python3 confusion.
- More explicit ownership of dirs in python_sitelib.
- Removed mixed use of tabs and spaces.
* Wed May 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-2
- python3 support.
* Wed May 09 2012 Ralph Bean <rbean@redhat.com> - 0.9.0-1
- Packaged latest upstream version.
- Removed unnecessary defattr and buildroot
- New dependency on python-six
* Fri Feb 3 2012 Ralph Bean <rbean@redhat.com> - 0.8.3-1
- Included tests in check section.
- More concise file ownership declarations.
- Resolved license ambiguity in upstream.
- Removed shebang from non-executable file.
* Mon Jan 30 2012 Ralph Bean <rbean@redhat.com> - 0.8.2-1
- Updated ansi2html version to latest 0.8.2.
- Added _bindir entry for the ansi2html console-script.
- Removed dependency on genshi.
- Removed references to now EOL fedora 12.
* Wed Sep 15 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.2-1
- Updated spec based on comments from Mark McKinstry
* Tue Sep 7 2010 Ralph Bean <ralph.bean@gmail.com> - 0.5.1-1
- Initial RPM packaging

