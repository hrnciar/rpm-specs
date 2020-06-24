%{?python_enable_dependency_generator}
%global pypi_name gTTS-token
# Needs access to Google Services so doesn't run in koji
%global with_tests 0

Name:           gtts-token
Version:        1.1.3
Release:        8%{?dist}
Summary:        Calculates a token to run the Google Translate text to speech
# LICENSE file is currently missing, already reported upstream
# https://github.com/Boudewijn26/gTTS-token/issues/5 
License:        MIT
URL:            https://github.com/boudewijn26/gTTS-token
Source0:        https://github.com/Boudewijn26/gTTS-token/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(requests)
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

%description
gTTS-token (Google Text to Speech token): A python implementation of the token 
validation of Google Translate

%package -n python3-gtts-token
Summary:  Python 3 lib to Calculates a token to run the Google Translate text to speech
%{?python_provide:%python_provide python3-gtts-token}

%description -n python3-gtts-token
gTTS-token (Google Text to Speech token): A python implementation of the token 
validation of Google Translate

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-gtts-token
%license LICENSE
%{python3_sitelib}/gTTS_token-*
%{python3_sitelib}/gtts_token/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-8
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.3-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.3-2
- Enable python dependency generator

* Mon Dec 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.3-1
- Update to 1.1.3

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.2-1
- Update to 1.1.2
- Drop python2 support

* Sat Jul 21 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-9
- Fix FTBFS, update spec to python2_sitelib

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuilt for Python 3.7

* Fri Feb 16 2018 2018 Lumír Balhar <lbalhar@redhat.com> - 1.1.1-6
- Fix directory ownership

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-2
- Package review updates

* Tue Feb  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.1-1
- initial packaging
