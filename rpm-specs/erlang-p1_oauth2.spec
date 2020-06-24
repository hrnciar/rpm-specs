%global srcname p1_oauth2


Name:       erlang-%{srcname}
Version:    0.6.5
Release:    4%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    An Oauth2 implementation for Erlang
URL:        https://github.com/processone/%{srcname}
Source0:    https://github.com/processone/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires: erlang-meck >= 0.8.3
BuildRequires: erlang-proper
BuildRequires: erlang-rebar


%description
This library is designed to simplify the implementation of the server side of
OAuth2. It is a fork of erlang-oauth2 by processone, and is needed by ejabberd.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%{rebar_compile}


%check
%{rebar_eunit}


%install
%{erlang_install}


%files
%license LICENSE
%doc README.md
%{erlang_appdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.5-3
- Rebuild for https://bugzilla.redhat.com/show_bug.cgi?id=1748545

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.5-1
- Update to 0.6.5 (#1713423).
- https://github.com/processone/p1_oauth2/blob/0.6.5/CHANGELOG.md

* Tue Apr 16 2019 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.4-1
- Update to 0.6.4 (#1683180).
- https://github.com/processone/p1_oauth2/blob/0.6.4/CHANGELOG.md

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 09 2018 Jeremy Cline <jeremy@jcline.org> - 0.6.3-1
- Update to v0.6.3 (#1572011).

* Sun Apr 01 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.2-4
- Backport a proper fix for the FTBFS for Erlang 20 (#1560321).

* Sun Mar 25 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.6.2-3
- Convert into a noarch package.
- Fix a FTBFS against Erlang 20 (#1560321).

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
