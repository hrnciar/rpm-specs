# Needs access to Google Services so doesn't run in koji
%global with_tests 0

Name:           gtts
Version:        2.1.1
Release:        3%{?dist}
Summary:        Create an mp3 file from spoken text via the Google TTS API

License:        MIT
URL:            https://github.com/pndurette/gTTS
Source0:        https://github.com/pndurette/gTTS/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-click
BuildRequires:  python3-gtts-token
BuildRequires:  python3-requests
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

Requires:       python3-gtts

%description
gTTS (Google Text to Speech): A cli interface for Google's Text to Speech API. 
Create an mp3 file with the gtts-cli command line utility. It allows 
unlimited lengths to be spoken by tokenizing long sentences where the speech 
would naturally pause.

%package -n python3-gtts
Summary:  Library for Python 3 to communicate with the Google gtts
%{?python_provide:%python_provide python3-gtts}

Requires: python3-beautifulsoup4
Requires: python3-click
Requires: python3-gtts-token
Requires: python3-requests
Requires: python3-six

%description -n python3-gtts
gTTS (Google Text to Speech): Python3 interface for Google's Text to Speech API. 
Create an mp3 file with the python3 gTTS module. It allows unlimited lengths to 
be spoken by tokenizing long sentences where the speech would naturally pause.

%prep
%setup -q -n gTTS-%{version}
sed -i '/twine/d' setup.cfg

%build
%py3_build

%install
%py3_install

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files
%{_bindir}/gtts-cli*

%files -n python3-gtts
%license LICENSE
%{python3_sitelib}/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1.1-3
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.1-1
- Update to 2.1.1

* Mon Jan  6 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-8
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-5
- Drop python2 support

* Tue Jul 17 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-4
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.7

* Wed Jun 20 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-1
- Update to 2.0.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.7

* Sat Jun 16 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.0-1
- Update to 2.0.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.2-1
- Update to 1.2.2

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 16 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.2.0-1
- Update to 1.2.0

* Sun Mar 19 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.8-3
- Depend on gtts-token

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.8-1
- Update to 1.1.8

* Wed Jan  4 2017 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.7-1
- initial packaging
