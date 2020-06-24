Name:           python-dotenv
Version:        0.13.0
Release:        2%{?dist}
Summary:        Add .env support to your Django/Flask apps in development and deployments

License:        BSD
URL:            https://github.com/theskumar/python-dotenv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-click
BuildRequires:  python3-devel
BuildRequires:  python3-ipython
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-sh

%description
Reads the key/value pair from .env file and adds them to environment variable.


%package -n     python3-dotenv
Summary:        %{summary}
Requires:       python3-click
Requires:       python3-setuptools
%{?python_provide:%python_provide python3-dotenv}

%description -n python3-dotenv
Reads the key/value pair from .env file and adds them to environment variable.


%prep
%autosetup
# Use the standard library mock
sed -i 's/import mock/from unittest import mock/' tests/test_*.py


%build
%py3_build


%install
%py3_install


%check
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONPATH=%{buildroot}%{python3_sitelib}
%{python3} -m pytest -v tests


%files -n python3-dotenv
%license LICENSE
%doc README.md
%{_bindir}/dotenv
%{python3_sitelib}/dotenv/
%{python3_sitelib}/python_dotenv-%{version}-py%{python3_version}.egg-info/


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-2
- Rebuilt for Python 3.9

* Mon May 04 2020 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-1
- Update to 0.13.0 (#1709002)
- Fix failing tests with click 7.1 (#1830984)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 06 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.1-1
- Initial package
