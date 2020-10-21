%global modname toot

Name:           %{modname}
Version:        0.27.0
Release:        1%{?dist}
Summary:        A CLI and TUI tool for interacting with Mastodon

License:        GPLv3
URL:            https://github.com/ihabunek/%{modname}
Source0:        https://github.com/ihabunek/%{modname}/releases/download/%{version}/%{modname}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/ihabunek/%{modname}/%{version}/LICENSE

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest} %{py3_dist requests} %{py3_dist wcwidth} %{py3_dist beautifulsoup4}

%description
Toot is a CLI and TUI tool for interacting with Mastodon instances
from the command line.

%prep
%autosetup -n %{modname}-%{version}
install -m 644 %{SOURCE1} .
rm -rf %{modname}.egg-info
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest

%files -n %{modname}
%{_bindir}/toot
%{python3_sitelib}/%{modname}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/%{modname}
%license LICENSE

%changelog
* Fri Aug 21 2020 Alessio <alciregi@fedoraproject.org> - 0.27.0-1
- Initial release
