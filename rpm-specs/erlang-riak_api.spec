%global realname riak_api
%global upstream basho


Name:		erlang-%{realname}
Version:	2.1.7
Release:	8%{?dist}
BuildArch:	noarch
Summary:	Riak Client APIs
License:	ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Patch1:		erlang-riak_api-0001-New-lager-API.patch
Patch2:		erlang-riak_api-0002-Suppress-warnings-about-deprecated-functions.patch
Patch3:		erlang-riak_api-0003-Remove-export_all-compiler-directive.patch
BuildRequires:	erlang-cuttlefish
BuildRequires:	erlang-exometer_core
BuildRequires:	erlang-lager
BuildRequires:	erlang-meck
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar
BuildRequires:	erlang-riak_core
BuildRequires:	erlang-riak_pb
BuildRequires:	erlang-webmachine


%description
This OTP application encapsulates services for presenting Riak's public-facing
interfaces. Currently this means a generic interface for exposing Protocol
Buffers-based services; HTTP services via Webmachine will be moved here at a
later time.


%prep
%autosetup -p1 -n %{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
install -D -p -m 644 priv/riak_api.schema %{buildroot}%{erlang_appdir}/priv/riak_api.schema


%check
%{erlang_test}


%files
%doc README.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-7
- Rebuilt with fixed Rebar

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-4
- Fix FTBFS with Erlang 20+

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 21 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.1.7-1
- Ver. 2.1.7

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.1.2-1
- Ver. 2.1.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-2
- Fix version mismatch

* Wed Jul 31 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.2-1
- Ver. 1.3.2

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-2
- Added builddep on os_mon

* Sun Mar 24 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.1-1
- Ver. 1.3.1

* Mon Mar 11 2013 Peter Lemenkov <lemenkov@gmail.com> - 1.3.0-1
- Ver. 1.3.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 12 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.1-1
- Ver. 1.2.1

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 1.2.0-1
- Initial build
