Name:           python-pydantic
Version:        1.3
Release:        5%{?dist}
Summary:        Data validation using Python type hinting

License:        MIT
URL:            https://github.com/samuelcolvin/pydantic
Source0:        https://github.com/samuelcolvin/pydantic/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# For check phase
BuildRequires:  python3-mypy
BuildRequires:  python3dist(pytest)

%description
Data validation and settings management using python type hinting.

%package -n     python3-pydantic
Summary:        %{summary}
%{?python_provide:%python_provide python3-pydantic}
 
Requires:       python3-email-validator >= 1.0.3
Requires:       python3-ujson >= 1.35

%description -n python3-pydantic
Data validation and settings management using python type hinting.

%prep
%autosetup -n pydantic-%{version}
# Remove bundled egg-info
rm -rf pydantic.egg-info

%build
%py3_build

# Docs are in MarkDown, and should be added when mkdocs is packaged.

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-pydantic
%license LICENSE
%doc README.md docs/
%{python3_sitelib}/pydantic
%{python3_sitelib}/pydantic-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3-5
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-3
- python-email_validator is now packaged as python-email-validator...

* Tue Jan 07 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-2
- Review fixes.

* Mon Jan 06 2020 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.3-1
- Update to 1.3.
- Review fixes.

* Sun Nov 24 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.1.1-1
- Update to 1.1.1.

* Sat Jul 27 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.31-1
- Initial package.
