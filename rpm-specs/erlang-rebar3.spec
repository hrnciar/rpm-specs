%global realname rebar3
%global otp_app_name rebar

# Technically we're noarch, but our install path is not.
%global debug_package %{nil}

# Bootstrapping
%global bootstrap 0

Name:     erlang-%{realname}
Version:  3.13.1
Release:  3%{?dist}
Summary:  Tool for working with Erlang projects
License:  ASL 2.0 and MIT
URL:      https://github.com/erlang/%{realname}
Source0:  %{url}/archive/%{version}.tar.gz#/%{realname}-%{version}.tar.gz
# Escript used to launch rebar3
Patch0:   add-rebar3-escript.patch
%if 0%{?bootstrap}
# I was not able to work with a non-archived source, so I built one with
# `fetch-precompiled-rebar3.sh`
Source1:  %{realname}-bin-%{version}.tar.gz
%else
BuildRequires:  erlang-rebar3
%endif

BuildArch: noarch
BuildRequires:  erlang-erts
BuildRequires:  perl-interpreter
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-ssl_verify_fun
BuildRequires:  erlang-certifi
BuildRequires:  erlang-providers
BuildRequires:  erlang-getopt
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-relx
BuildRequires:  erlang-cf
BuildRequires:  erlang-cth_readable
BuildRequires:  erlang-eunit_formatters
BuildRequires:  erlang-hex_core
Requires:  erlang-erts
Requires:  erlang-erlware_commons
Requires:  erlang-ssl_verify_fun
Requires:  erlang-certifi
Requires:  erlang-providers
Requires:  erlang-getopt
Requires:  erlang-bbmustache
Requires:  erlang-relx
Requires:  erlang-cf
Requires:  erlang-cth_readable
Requires:  erlang-eunit_formatters
Requires:  erlang-hex_core

%description
Rebar3 is an Erlang tool that makes it easy to create, develop, and release
Erlang libraries, applications, and systems in a repeatable manner.

%prep
%setup -q -n %{realname}-%{version}
%if 0%{?bootstrap}
%setup -q -D -T -a 1 -n %{realname}-%{version}
%endif
%patch0 -p1

%build
ebin_paths=$(perl -e 'print join(":", grep { !/rebar/} (glob("%{_libdir}/erlang/lib/*/ebin"), glob("%{_datadir}/erlang/lib/*/ebin")))')

%if 0%{?bootstrap}
./precompiled/%{realname} bare compile --paths $ebin_paths --separator :
%else
%{realname} bare compile --paths $ebin_paths --separator :
%endif

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
mkdir -p %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/priv/
mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m755 %{realname} %{buildroot}%{_bindir}/%{realname}
install -p -m644 ebin/*.beam %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m644 ebin/%{otp_app_name}.app %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/ebin/
install -p -m755 -d priv/* %{buildroot}%{_datadir}/erlang/lib/%{realname}-%{version}/priv/
install -p -m644 manpages/%{realname}.1 %{buildroot}%{_mandir}/man1/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{realname}
%{_datadir}/erlang/lib/%{realname}-%{version}
%{_mandir}/man1/%{realname}.1*

%changelog
* Fri Mar 13 2020 Timothée Floure <fnux@fedoraproject.org> - 3.13.1-1
- New upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 16 2019 Timothée Floure <fnux@fedoraproject.org> - 3.11.1-1
- New upstream release

* Fri May 31 2019 Timothée Floure <fnux@fedoraproject.org> - 3.10.1-1
- Rebase on latest upstream release

* Thu May 30 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-4
- Rebootstrap from upstream rebar 3.8.0 binary (see packaging-comittee/#889 on pagure)

* Fri Mar 08 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-3
- Add dependency on erlang-hex_core
- Load noarch erlang dependencies during compilation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Timothée Floure <fnux@fedoraproject.org> - 3.8.0-1
- New upstream release

* Tue Dec 18 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-3
- Switch to noarch in accord with 'Changes/TrueNoarchErlangPackages'

* Wed Dec 12 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-2
- Disable bootstaping following initial build in rawhide

* Fri Oct 12 2018 Timothée Floure <fnux@fedoraproject.org> - 3.6.2-1
- Let there be package
