%{?python_enable_dependency_generator}
%{!?_httpd_modconfdir: %{expand: %%global _httpd_modconfdir %%{_sysconfdir}/httpd/conf.d}}
Name:           oraculum
# Don't forget to also change oraculum/__init__.py
Version:        0.0.3
Release:        3%{?dist}
Summary:        Backend and API for Fedora QA Dashboard

License:        GPLv2+
URL:            https://pagure.io/fedora-qa/oraculum
Source0:        https://releases.pagure.org/fedora-qa/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Backend and API for Fedora QA Dashboard

%prep
%setup -q

%build
%py3_build

%install
%py3_install

# apache and wsgi settings
mkdir -p %{buildroot}%{_datadir}/oraculum
cp -p conf/oraculum.wsgi %{buildroot}%{_datadir}/oraculum/.

mkdir -p %{buildroot}%{_sysconfdir}/oraculum
install conf/settings.py.example %{buildroot}%{_sysconfdir}/oraculum/settings.py

install -d -m 755 %{buildroot}%{_httpd_modconfdir}
install -p -m 644 conf/oraculum.conf %{buildroot}%{_httpd_modconfdir}/oraculum.conf

%files
%doc README.md conf/*
%{python3_sitelib}/oraculum/
%{python3_sitelib}/*.egg-info/

%{_bindir}/oraculum
%dir %{_sysconfdir}/oraculum
%dir %{_datadir}/oraculum
%{_datadir}/oraculum/*

%config(noreplace) %{_sysconfdir}/oraculum/settings.py
%config(noreplace) %{_httpd_modconfdir}/oraculum.conf

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.0.3-2
- Rebuilt for Python 3.9

* Mon Feb 10 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.0.3-1
- Release 0.0.3

* Fri Feb 15 2019 Lukas Brabec <lbrabec@redhat.com> - 0.0.2-1
- Bump to 0.0.2

* Wed Feb 13 2019 Lukas Brabec <lbrabec@redhat.com> - 0.0.1-3
- Better summary and description

* Thu Feb 07 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.0.1-2
- Improved packaging

* Thu Feb 06 2014 Josef Skladanka <jskladan@redhat.com> - 0.0.1-1
- initial packaging
