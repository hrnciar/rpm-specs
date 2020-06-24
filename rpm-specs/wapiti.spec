%bcond_with tests

Name:           wapiti
Version:        3.0.2
Release:        4%{?dist}
Summary:        A web application vulnerability scanner

# wapiti is GPLv2+
# PyNarcissus is MPL 1.1/GPL 2.0+/LGPL 2.1
# Kube CSS frameworka nd jQuery are MIT
License:        GPLv2+ and MIT
URL:            http://wapiti.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{version}/%{name}3-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-responses
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest-runner

%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  php-cli
%endif

%description
Wapiti allows you to audit the security of your web applications. It performs
"black-box" scans, i.e. it does not study the source code of the application 
but will scans the web pages of the deployed web app, looking for scripts and 
forms where it can inject data. Once it gets this list, Wapiti acts like a 
fuzzer, injecting payloads to see if a script is vulnerable.

%prep
%autosetup -n %{name}3-%{version}
find -name '*.py' | xargs sed -i '/^#!\//, 1d'

%build
%py3_build

%install
%py3_install
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/

%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests
%endif

%files
%doc README.md doc/FAQ.md doc/example.txt
%license doc/COPYING
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}*
%{python3_sitelib}/wapitiCore/
%{python3_sitelib}/%{name}3-%{version}-py*.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-4
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.2-2
- Adjust BRs
- Update the source URL
- Better use of wildcards (rhbz#1787225)

* Wed Jan 01 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.0.2-1
- Initial package for Fedora
