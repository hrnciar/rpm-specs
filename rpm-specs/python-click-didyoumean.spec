# Created by pyp2rpm-3.3.4
%global pypi_name click-didyoumean

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Enable git-like did-you-mean feature in click

License:        MIT
URL:            https://github.com/timofurrer/click-didyoumean
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

# Patches adapt tests to a newer python-click (present in Fedora)
Patch0:         %{url}/pull/4.patch
Patch1:         0001-Fix-tests-some-more.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-click
BuildRequires:  python3-pytest
BuildRequires:  python3-prompt-toolkit

%description
%{summary}

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/click_didyoumean/
%{python3_sitelib}/click_didyoumean-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Sep 29 2020 František Zatloukal <fzatlouk@redhat.com> - 0.0.3-1
- Initial package.
