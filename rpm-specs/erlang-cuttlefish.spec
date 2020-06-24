%global realname cuttlefish
%global upstream basho


Name:		erlang-%{realname}
Version:        2.0.11
Release:        10%{?dist}
BuildArch:      noarch
Summary:        A library for dealing with sysctl-like configuration syntax
License:        ASL 2.0
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	%{realname}.escript
Patch1:		erlang-cuttlefish-0001-Disable-escript-generation.patch
Patch2:		erlang-cuttlefish-0002-No-rebar_mustache-available.patch
Patch3:		erlang-cuttlefish-0003-Double-quotes-escaping-is-no-longer-necessary.patch
# The next 5 patches are for this issue and PR:
# https://github.com/basho/cuttlefish/issues/237
# https://github.com/basho/cuttlefish/pull/241
Patch4:		erlang-cuttlefish-0004-Do-not-warn-on-export-all.patch
Patch5:		erlang-cuttlefish-0005-Erlang-20-compilation-export-all-failure.patch
Patch6:		erlang-cuttlefish-0006-Add-recent-otp-versions-to-rebar.config.patch
Patch7:		erlang-cuttlefish-0007-Add-nowarn_export_all-to-tests-to-suppress-errors-fo.patch
Patch8:		erlang-cuttlefish-0008-Make-escript-work-on-OTP20.patch
Patch9:		erlang-cuttlefish-0009-erlang-get_stacktrace-0-deprecated.patch
BuildRequires:  erlang-lager
BuildRequires:  erlang-rebar


%description
Cuttlefish is a library for Erlang applications that wish to walk the fine line
between Erlang app.configs and a sysctl-like syntax. The name is a pun on the
pronunciation of 'sysctl' and jokes are better explained.


%prep
%autosetup -p1 -n %{realname}-%{version}
# Temporarily remove rebar plugin until we start packaging rebar plugins
rm -f src/cuttlefish_rebar_plugin.erl


%build
%{erlang_compile}


%install
%{erlang_install}
# Install cuttlefish script itself
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{realname}



%check
%{erlang_test}


%files
%doc README.md
%{_bindir}/%{realname}
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Lemenkov <lemenkov@gmail.com> - 2.0.11-9
- Fix deprecation warning

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Peter Lemenkov <lemenkov@gmail.com> - 2.0.11-1
- Ver. 2.0.11

* Tue Nov 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.10-1
- Ver. 2.0.10

* Tue Mar 15 2016 Peter Lemenkov <lemenkov@gmail.com> - 2.0.6-1
- Initial packaging
