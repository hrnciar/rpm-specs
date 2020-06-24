%{?python_enable_dependency_generator}
%global with_tests 0

Name:           adapt
Version:        0.3.5
Release:        2%{?dist}
Summary:        Mycroft's Adapt Intent Parser
License:        ASL 2.0
URL:            https://adapt.mycroft.ai/
Source0:        https://github.com/MycroftAI/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  libicu-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%if 0%{?with_tests}
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pyee) = 5
BuildRequires:  python3-pep8
%endif

%description
The Adapt Intent Parser is a flexible and extensible intent definition and 
determination framework. It is intended to parse natural language text into a 
structured intent that can then be invoked programatically.

%package -n python3-adapt
Summary:        A python3 library for Adapt Intent Parser
%{?python_provide:%python_provide python3-adapt}

%description -n python3-adapt
A python3 library for Adapt Intent Parser.

%prep
%autosetup -p1 -n %{name}-release-v%{version}
rm -rf adapt-parser.egg-info
sed -i 's#pyee==5.0.0#pyee>=5.0.0#' requirements.txt
sed -i 's#pyee==5.0.0#pyee>=5.0.0#' setup.py

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-adapt
%license LICENSE.md
%{python3_sitelib}/%{name}_parser-%{version}*
%{python3_sitelib}/%{name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.5-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.5-1
- Update to 0.3.5

* Sat Feb  1 2020 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.4-3
- Handle newer pyee

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.4-1
- Update to 0.3.4

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-4
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul  2 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.3-1
- Update to 0.3.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.2-2
- Enable python dependency generator

* Sat Dec 22 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.2-1
- Update to 0.3.2
- License changed to Apache 2.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-6
- Rebuilt for Python 3.7

* Sun May 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-5
- Drop python2 support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.3.0-3
- Fix ambiguous Python 2 dependency declarations
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.3.0-1
- Initial package
