%if 0%{?fedora} > 27 || 0%{?rhel} > 7
# Build python3
%global with_python3 1
%global PYTHONDIR %{python3_sitelib}
%else
%global with_python3 0
%global PYTHONDIR %{python2_sitelib}
%endif

Summary: Web page with summary of ABRT services
Name: abrt-server-info-page
Version: 1.8
Release: 3%{?dist}
License: GPLv3+
URL: https://github.com/marusak/abrt-server-info-page
# source is created by:
# git clone
# cd abrt-server-info-page; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%if 0%{?with_python3}
BuildRequires: python3-devel
%else
BuildRequires: python2-devel
%endif

%if 0%{?with_python3}
Requires: python3-flask >= 0.10
Requires: python3-mod_wsgi
%else
Requires: python-flask >= 0.10
Requires: mod_wsgi
%endif
Requires: httpd
Requires(post): systemd

%description
Web page for use as front page of ABRT servers. Contains information about
ABRT's products.

%prep
%setup -q

%install
sed -i "s|@PYTHONDIR@|%{PYTHONDIR}|g" config/abrt-server-info-page.conf
mkdir -p %{buildroot}
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/js
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/css
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static/fonts
mkdir -p %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/templates
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
cp -a abrt_server_info_page.py %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a abrt_server_info_page.wsgi %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a config.py %{buildroot}/%{PYTHONDIR}/abrt-server-info-page
cp -a config/abrt-server-info-page.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/
cp -a templates/index.html %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/templates
cp -a static/* %{buildroot}/%{PYTHONDIR}/abrt-server-info-page/static

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server-info-page.conf
%{PYTHONDIR}/abrt-server-info-page

%license LICENSE

%post
systemctl condrestart httpd

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.8-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Martin Kutlak <mkutlak@redhat.com> 1.8-1
- New upstream release 1.8.1
- FAF rename to ABRT Analytics

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 07 2019 Martin Kutlak <mkutlak@redhat.com> 1.7-1
- Migrate to python3 for F28+ and RHEL8+
- add releaser for f29
* Wed Apr 18 2018 Miroslav Suchý <msuchy@redhat.com> 1.6-1
- fix dependencies on F27- and RHEL (msuchy@redhat.com)

* Wed Mar 21 2018 Miroslav Suchý <msuchy@redhat.com> 1.5-1
- require systemd
- Update Python 2 dependency declarations to new packaging standards
  (mmarusak@redhat.com)

* Thu Jan 11 2018 Martin Kutlak <mkutlak@redhat.com> 1.4-1
- swap links (msuchy@redhat.com)

* Wed Apr 12 2017 Miroslav Suchý <msuchy@redhat.com> 1.3-1
- add link to wiki (msuchy@redhat.com)
- add missing quotes (msuchy@redhat.com)
- Add retrace server's disclaimer (mmarusak@redhat.com)

* Sat Feb 04 2017 Matej Marusak <marusak.matej@gmail.com> 1.2-1
- Add license into specfile (marusak.matej@gmail.com)
- Add BuildRequires into specfile (marusak.matej@gmail.com)
- Create LICENSE (marusak.matej@gmail.com)
- Fix wrong command in specfile (mmarusak@redhat.com)
- Add README (marusak.matej@gmail.com)
- Remove unused BuildRequires from specfile (marusak.matej@gmail.com)
* Thu Jan 19 2017 Matej Marusak <mmarusak@redhat.com> 1.1-1
- Initial package
