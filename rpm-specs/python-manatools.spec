%global module manatools

Name:           python-%{module}
Version:        0.0.3
Release:        1%{?dist}

Summary:        A Python framework to build ManaTools applications
License:        LGPLv2+
URL:            https://github.com/manatools/python-manatools
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# Backports from upstream
Patch0001:      0001-Drop-argparse-as-a-dependency.patch

BuildArch:      noarch

%description
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%package -n python3-%{module}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-yui
%{?python_provide:%python_provide python3-%{module}}
Requires:       python3-yui
Recommends:     (libyui-mga-qt if qt5-qtbase-gui)
Recommends:     (libyui-mga-gtk if gtk3)

%description -n python3-%{module}
Python ManaTools aim is to help in writing tools based on libYui
(SUSE widget abstraction library), to be collected under the
ManaTools banner and hopefully with the same look and feel.

Every output module supports the Qt, GTK, and ncurses interfaces.

%prep
%autosetup -p1

sed -i 's|0.0.1|%{version}|' manatools/version.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{module}
%doc README.md NEWS
%license LICENSE
%{python3_sitelib}/%{module}/
%{python3_sitelib}/python_manatools-%{version}-py%{python3_version}.egg-info

%changelog
* Sun Oct 04 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.3-1
- Initial package

