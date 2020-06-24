%global sum Python Twilio Helper Library

%global desc \
The Twilio REST SDK simplifies the process of making calls using the Twilio \
REST API. \
The Twilio REST API lets to you initiate outgoing calls, list previous calls, \
and much more.


Name:           python-twilio
Version:        6.32.0
Release:        3%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://www.github.com/twilio/twilio-python
Source0:        https://github.com/twilio/twilio-python/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist nose}
BuildRequires:  %{py3_dist pytz}
BuildRequires:  %{py3_dist six}
BuildRequires:  %{py3_dist mock}
BuildRequires:  %{py3_dist pyjwt}
BuildRequires:  %{py3_dist requests}
BuildRequires:  %{py3_dist pyopenssl}

%description
%{desc}

#python2 subpackage
%package -n python3-twilio
Summary:        %{sum}

Requires:   %{py3_dist six}
Requires:   %{py3_dist requests}
Requires:   %{py3_dist pyjwt}
Requires:   %{py3_dist pytz}

%{?python_provide:%python_provide python3-twilio}

%description -n python3-twilio
%{desc}



%prep
%autosetup -n twilio-python-%{version}

%build

%py3_build


%install
%py3_install


%check

%{__python3} setup.py test


%files -n python3-twilio
%license LICENSE.md
%doc README.md examples
%{python3_sitelib}/*


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 6.32.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.32.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 17 2019 Michael Cullen <michael@cullen-online.com> - 6.32.0-1
- Updated to 6.32.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.29.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.29.1-2
- Rebuilt for Python 3.8

* Fri Aug 02 2019 Michael Cullen <michael@cullen-online.com> - 6.29.1-1
- Updated to 6.29.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.27.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Michael Cullen <michael@cullen-online.com> - 6.10.3-1
- Updated to 6.27.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.14.7-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.14.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 6.14.7-1
- Update to 6.14.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 6.10.3-2
- Rebuilt for Python 3.7

* Fri Feb 16 2018 Michael Cullen <michael@cullen-online.com> - 6.10.3-1
- new version

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 10 2017 Michael Cullen <michael@cullen-online.com> - 6.9.1-1
- new version

* Tue Nov 21 2017 Michael Cullen <michael@cullen-online.com> - 6.9.0-1
- new version

* Mon Nov 06 2017 Michael Cullen <michael@cullen-online.com> - 6.8.3-1
- new version

* Tue Oct 24 2017 Michael Cullen <michael@cullen-online.com> - 6.8.1-1
- Updated to a new version
* Sat Oct 14 2017 Michael Cullen <michael@cullen-online.com> - 6.8.0-1
- Updated to a new version
- Dealt with some review comments
* Sun Oct 08 2017 Michael Cullen <michael@cullen-online.com> - 6.7.1-1
- Updated to a new version
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> - 6.6.0-2
- Various improvements to match example better
* Sat Aug 26 2017 Michael Cullen <michael@cullen-online.com> - 6.6.0-1
- Intial Packaging
