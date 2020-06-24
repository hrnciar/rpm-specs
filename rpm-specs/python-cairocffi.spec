%global srcname cairocffi

Name:           python-cairocffi
Version:        1.1.0
Release:        3%{?dist}
Summary:        cffi-based cairo bindings for Python
License:        BSD
URL:            https://pypi.python.org/pypi/cairocffi/
Source0:        %{pypi_source}
Patch0:         python-cairocffi-disable-flake8-isort-for-pytest.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-xcffib >= 0.3.2
BuildRequires:  cairo-devel
# required to run the test suite
BuildRequires:  gdk-pixbuf2
BuildRequires:  gdk-pixbuf2-modules

%global _description\
cairocffi is a CFFI-based drop-in replacement for Pycairo, a set of\
Python bindings and object-oriented API for cairo.  Cairo is a 2D\
vector graphics library with support for multiple backends including\
image buffers, PNG, PostScript, PDF, and SVG file output.

%description %_description

%package -n python3-cairocffi
Summary:        cffi-based cairo bindings for Python
Requires:       python3-cffi
Requires:       cairo
# required by cairocffi.pixbuf
Requires:       python3-xcffib >= 0.3.2
%{?python_provide:%python_provide python3-cairocffi}

%description -n python3-cairocffi %_description

%prep
%autosetup -n cairocffi-%{version}
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-cairocffi
%license LICENSE
%doc README.rst
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Felix Schwarz <fschwarz@fedoraproject.org> - 1.1.0-1
- Update to latest release
- require python3-xcffib at runtime (#1698217)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.9.0-1
- Update to latest release
- Modernize spec file a bit

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.2-16
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Nov 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-15
- Don't use unversioned Python command

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-13
- Rebuilt for Python 3.7
- Drop unused and unavailable BR python2-xcffib

* Tue Mar 13 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.7.2-12
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.2-10
- Python 2 binary package renamed to python2-cairocffi
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 08 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.7.2-5
- Add cairo to Requires for python3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Adam Williamson <awilliam@redhat.com> - 0.7.2-2
- buildrequires python-xcffib (for xcb support)

* Fri Oct 16 2015 Adam Williamson <awilliam@redhat.com> - 0.7.2-1
- bump to latest upstream release (RHBZ #1249821)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.6-2
- Build and ship HTML docs instead of their source
- Mark LICENSE as %%license

* Mon Nov 03 2014 Eric Smith <brouhaha@fedoraproject.org> 0.6-1
- Update to latest upstream.

* Mon Aug 25 2014 Eric Smith <brouhaha@fedoraproject.org> 0.5.4-1
- Update to latest upstream.
- No python3 in EL7.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Jul 26 2013 Eric Smith <brouhaha@fedoraproject.org> 0.5.1-3
- For EL6, remove require of gdk-pixbuf2.

* Tue Jul 23 2013 Eric Smith <brouhaha@fedoraproject.org> 0.5.1-2
- Added Python 3 support.

* Sun Jul 21 2013 Eric Smith <brouhaha@fedoraproject.org> 0.5.1-1
- initial version
