%global         github_name linux-cli
%global         srcname protonvpn_cli

Name:           protonvpn-cli
Version:        2.2.4
Release:        1%{?dist}
Summary:        Linux command-line client for ProtonVPN written in Python

License:        GPLv3
URL:            https://github.com/ProtonVPN/%{github_name}
Source:         %{url}/archive/v%{version}/%{github_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-devel

Requires:       openvpn
%if 0%{?fedora} || 0%{?.el8}
Recommends:     dialog
Recommends:     NetworkManager-openvpn
Suggests:       NetworkManager-openvpn-gnome
%else
Requires:       dialog
%endif

%description
The official Linux CLI for ProtonVPN.

ProtonVPN-CLI is a full rewrite of the bash protonvpn-cli in Python, which adds
more features and functionality with the purpose of improving readability,
speed and reliability.

ProtonVPN-CLI features a DNS Leak Protection feature, which makes sure that
your online traffic uses ProtonVPN's DNS Servers. This prevents third parties
(like your ISP) from being able to see your DNS queries (and, therefore, your
browsing history).


%prep
%autosetup -n %{github_name}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/protonvpn


%changelog
* Mon Jun 01 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.4-1
- Enhancement: Option to define API domain via config
- Enhancement: Improve wording on connection failure
- Bug fix: Error during connection when IPv6 is disabled system-wide
- Bug fix: Unable to change DNS in containers
- Bug fix: pgrep not working on some distros
- Bug fix: Failing to connect when choosing a server via dialog menu

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.2-8
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-7
- Approved package for official Fedora repositories
- Remove Requires handled by Python dependency generator (BZ #1809814)

* Fri Mar 27 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-6
- Remove python3-dialog as dependency (already Required automatically)

* Mon Mar 16 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-5
- Remove tags not used in Fedora packages
- Add missing dependencies tracked in upstream requirements.txt

* Tue Mar 03 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-4
- Adhere to Fedora Packaging Guidelines via fedora-review

* Wed Feb 26 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.2-1
- Update to latest upstream

* Mon Feb 3 2020 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.1-1
- Update to latest upstream

* Wed Dec 25 2019 Justin W. Flory <jflory7@fedoraproject.org> - 2.2.0-1
- First protonvpn-cli package
