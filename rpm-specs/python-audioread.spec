%if 0%{?fedora} < 32
%global         py2 1
%endif

Summary:        Multi-library, cross-platform audio decoding in Python
Name:           python-audioread
Version:        2.1.8
Release:        6%{?dist}
License:        MIT
URL:            http://pypi.python.org/pypi/audioread/
Source0:        https://files.pythonhosted.org/packages/source/a/audioread/audioread-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?py2}
BuildRequires:  python2-devel
Buildrequires:  python2-pytest-runner
%endif
BuildRequires:  python3-devel
Buildrequires:  python3-pytest-runner
%global _description \
Decode audio files using whichever backend is available. Among\
currently supports backends are\
 o Gstreamer via PyGObject\
 o MAD via the pymad bindings\
 o FFmpeg or Libav via its command-line interface\
 o The standard library wave, aifc, and sunau modules
%description %_description

%if 0%{?py2}
%package     -n python2-audioread
Summary:        Multi-library, cross-platform audio decoding in Python
Requires:       python2-gobject
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
%{?python_provide:%python_provide python2-audioread}
%description -n python2-audioread %_description
%endif

%package    -n  python3-audioread
Summary:        Multi-library, cross-platform audio decoding in Python
Requires:       python3-gobject
Requires:       gstreamer1
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
%{?python_provide:%python_provide python3-audioread}
%description -n python3-audioread %_description

%prep
%setup -q -n audioread-%{version}

%build
%{?py2:%{py2_build}}
%{py3_build}

%install
%{?py2:%{py2_install}}
%{py3_install}

%if 0%{?py2}
%files -n python2-audioread
%doc README.rst decode.py
%{python2_sitelib}/audioread/
%{python2_sitelib}/audioread-%{version}-*.egg-info
%endif

%files -n python3-audioread
%doc README.rst decode.py
%{python3_sitelib}/audioread/
%{python3_sitelib}/audioread-%{version}-*.egg-info

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.8-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 01 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.8-3
- No Python 2 in newer Fedoras

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.8-2
- Rebuilt for Python 3.8

* Fri Aug 09 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.8-1
- 2.1.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 2.1.7-1
- 2.1.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.1.6-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.1.6-1
- 2.1.6

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.1.5-1
- 2.1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 15 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-3
- Ranaming of pygobject3 was done in F23 (rhbz#1308613)

* Tue Feb 02 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-2
- Add proper python*-audioread provides

* Mon Feb 01 2016 Terje Rosten <terje.rosten@ntnu.no> - 2.1.2-1
- 2.1.2

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Kalev Lember <kalevlember@gmail.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon Nov 18 2013 Terje Røsten <terje.rosten@ntnu.no> - 1.0.1-1
- 1.0.1
- Python 3 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 24 2012 Terje Røsten <terje.rosten@ntnu.no> - 0.6-1
- initial package

