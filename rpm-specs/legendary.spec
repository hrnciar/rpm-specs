Name:           legendary
Version:        0.0.19
Release:        1%{?dist}
Summary:        Free and open-source replacement for the Epic Games Launcher
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/derrod/legendary
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3dist(requests)

Requires:       python3-requests

%description
Legendary is an open-source game launcher that can download and install games
from the Epic Games Store on Linux and Windows. It's name as a tongue-in-cheek
play on tiers of item rarity in many MMORPGs.


%prep
%autosetup -p1

# E: non-executable-script
for lib in %{name}/{*.py,downloader/*.py,lfs/*.py,models/*.py}; do
  sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
  touch -r $lib $lib.new &&
  mv $lib.new $lib
done


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}*.egg-info/
%{python3_sitelib}/%{name}/


%changelog
* Sun Jun 14 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.19-1
- Update to 0.0.19

* Tue Jun 02 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.18-1
- Update to 0.0.18

* Sun May 31 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.17-1
- Update to 0.0.17

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.16-1
- Update to 0.0.16

* Sat May 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.15-1
- Update to 0.0.15

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.14-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.14-1
- Update to 0.0.14

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.13-1
- Update to 0.0.13

* Fri May 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.11-1
- Update to 0.0.11

* Tue May 05 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.10-1
- Update to 0.0.10

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.9-1
- Update to 0.0.9

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.8-1
- Update to 0.0.8

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.7-1
- Update to 0.0.7

* Thu Apr 30 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.6-2
- Initial package
