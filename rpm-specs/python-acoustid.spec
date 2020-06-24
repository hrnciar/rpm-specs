%global oname   pyacoustid

%if 0%{?fedora} < 32
%global         py2 1
%endif

Summary:        Python bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Name:           python-acoustid
Version:        1.2.0
Release:        2%{?dist}
License:        MIT
URL:            http://pypi.python.org/pypi/pyacoustid
Source0:        https://files.pythonhosted.org/packages/source/p/%{oname}/%{oname}-%{version}.tar.gz
BuildArch:      noarch
%{?py2:BuildRequires:  python2-devel}
BuildRequires:  python3-devel

%description
Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package
provides Python bindings for both the fingerprinting algorithm
library, which is written in C but portable, and the Web service,
which provides fingerprint look ups.

%if 0%{?py2}
%package -n    python2-acoustid
Summary:       Python bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Requires:      libchromaprint
Requires:      python2-audioread
%{?python_provide:%python_provide python2-acoustid}
%description -n python2-acoustid
Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package
provides Python bindings for both the fingerprinting algorithm
library, which is written in C but portable, and the Web service,
which provides fingerprint look ups.
%endif

%package -n    python3-acoustid
Summary:       Python bindings for Chromaprint acoustic fingerprinting and the Acoustid API
Requires:      libchromaprint
Requires:      python3-audioread
%{?python_provide:%python_provide python3-acoustid}
%description -n python3-acoustid
Chromaprint and its associated Acoustid Web service make up a
high-quality, open-source acoustic fingerprinting system. This package
provides Python bindings for both the fingerprinting algorithm
library, which is written in C but portable, and the Web service,
which provides fingerprint look ups.

%prep
%setup -q -n %{oname}-%{version}

%build
%{?py2:%{py2_build}}
%{py3_build}

%install
%{?py2:%{py2_install}}
%{py3_install}

%if 0%{?py2}
%files -n python2-acoustid
%doc README.rst aidmatch.py fpcalc.py
%{python2_sitelib}/acoustid.py*
%{python2_sitelib}/chromaprint.py*
%{python2_sitelib}/pyacoustid-%{version}-*.egg-info/
%endif

%files -n python3-acoustid
%doc README.rst aidmatch.py fpcalc.py
%{python3_sitelib}/acoustid.py
%{python3_sitelib}/chromaprint.py
%{python3_sitelib}/pyacoustid-%{version}-*.egg-info/
%{python3_sitelib}/__pycache__/acoustid.*.py*
%{python3_sitelib}/__pycache__/chromaprint.*.py*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 31 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.1.7-4
- No Python 2 in newer Fedoras

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 25 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.1.7-1
- 1.1.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-7
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.5-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 09 2017 Terje Rosten <terje.rosten@ntnu.no> - 1.1.5-1
- 1.1.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.1.0-1
- 1.1.0
- Python 3 subpackage

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Sep 16 2012 Terje Røsten <terje.rosten@ntnu.no> - 0.7-3
- Fix req.

* Mon Aug 27 2012 Terje Røsten <terje.rosten@ntnu.no> - 0.7-2
- Convert spec to utf-8
- Fix spelling

* Fri Aug 24 2012 Terje Røsten <terje.rosten@ntnu.no> - 0.7-1
- initial package
