%global realname eflame
%global upstream slfritchie


Name:		erlang-%{realname}
Version:	0
Release:	0.16.gita085181%{?dist}
BuildArch:	noarch
Summary:	Flame Graph profiler for Erlang
License:	MIT
URL:		https://github.com/%{upstream}/%{realname}
VCS:		scm:git:https://github.com/%{upstream}/%{realname}.git
#Source0:	https://github.com/%{upstream}/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}/archive/a08518142126f5fc541a3a3c4a04c27f24448bae/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar
BuildRequires:	perl-generators
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))


%description
Flame Graph profiler for Erlang.


%prep
%setup -q -n %{realname}-a08518142126f5fc541a3a3c4a04c27f24448bae


%build
%{erlang_compile}


%install
%{erlang_install}

install -D -p -m 0755 flamegraph.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.pl
install -D -p -m 0755 flamegraph.riak-color.pl %{buildroot}%{erlang_appdir}/bin/flamegraph.riak-color.pl


%check
%{erlang_test}


%files
%license LICENSE
%doc README.md README-Riak-Example.md
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.15.gita085181
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 05 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.13.gita085181
- Perl 5.30 rebuild (2)

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.12.gita085181
- Perl 5.30 rebuild

* Wed Feb 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0-0.11.gita085181
- Switch to noarch

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.8.gita085181
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.4.gita085181
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gita085181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0-0.2.gita085181
- Perl 5.24 rebuild

* Fri Apr 22 2016 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.gita085181
- Initial build

