%global realname relx
%global upstream erlware

Name:     erlang-%{realname}
Version:  3.32.1
Release:  3%{?dist}
BuildArch: noarch
Summary:  Release assembler for Erlang/OTP Releases
License:  ASL 2.0
URL:      https://github.com/%{upstream}/%{realname}
Source0:  https://github.com/%{upstream}/%{realname}/archive/v%{version}/%{realname}-v%{version}.tar.gz
BuildRequires:  erlang-rebar
BuildRequires:  erlang-providers
BuildRequires:  erlang-erlware_commons
BuildRequires:  erlang-cf
BuildRequires:  erlang-bbmustache
BuildRequires:  erlang-getopt
Requires:       erlang-rebar
Requires:       erlang-providers
Requires:       erlang-erlware_commons
Requires:       erlang-cf
Requires:       erlang-getopt
Requires:       erlang-bbmustache

%description
Relx assembles releases for an Erlang/OTP release. Given a release
specification and a list of directories in which to search for OTP applications
it will generate a release output.

%prep
%autosetup -n %{realname}-%{version}

# FIXME: for some reason eunit fails to compile test/rlx_test_utils.erl when
# using rebar2. We should be able to get ride of this line once rebar3 is
# properly packaged.
rm test/rlx_test_utils.erl

# FIXME: this module depends on rlx_test_utils, see above comment.
rm test/rlx_depsolver_tester.erl

%build
%{erlang_compile}

%install
%{erlang_install}

%check
%{erlang_test}

%files
%license LICENSE.md
%doc README.md examples
%{erlang_appdir}/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.32.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 04 2019 Timothée Floure <fnux@fedoraproject.org> - 3.32.1-1
- New upstream release

* Wed May 15 2019 Timothée Floure <fnux@fedoraproject.org> - 3.31.0-1
- New upstream release

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 3.28.0-1
- New upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Randy Barlow <bowlofeggs@fedoraproject.org> - 3.26.0-3
- Convert into a noarch package.
- Rebuild against the noarch bbmustache (#1638979).

* Thu Oct 11 2018 Timothée Floure <fnux@fedoraproject.org> - 3.26.0-2
- Fix runtime dependency on bbmustache

* Sun Jul 15 2018 Timothée Floure <fnux@fedoraproject.org> - 3.26.0-1
- Let there be package
