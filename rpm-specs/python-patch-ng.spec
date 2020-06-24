%global appname patch-ng

%global appsum Library to parse and apply unified diffs
%global appdesc Fork of the original python-patch library to parse \
and apply unified diffs

Name: python-%{appname}
Version: 1.17.2
Release: 3%{?dist}
Summary: %{appsum}

# Separate license file is currently missing:
# https://github.com/conan-io/python-patch-ng/issues/8
License: MIT
URL: https://github.com/conan-io/%{name}
Source0: %{pypi_source %{appname}}
BuildArch: noarch

BuildRequires: python3-devel

%description
%{appdesc}.

%package -n python3-%{appname}
Summary: %{appsum}
%{?python_provide:%python_provide python3-%{appname}}

%description -n python3-%{appname}
%{appdesc}.

%prep
%autosetup -n %{appname}-%{version}
sed -e '/\/usr\/bin\/env/d' -i patch_ng.py

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{appname}
%doc README.md
%{python3_sitelib}/patch_ng.py
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/patch_ng-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.17.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 25 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.17.2-1
- Initial SPEC release.
