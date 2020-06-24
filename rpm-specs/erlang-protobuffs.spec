%global realname protobuffs
%global upstream basho


Name:		erlang-%{realname}
Version:	0.9.1
Release:	5%{?dist}
BuildArch:	noarch
Summary:	A set of Protocol Buffers tools and modules for Erlang applications
License:	ASL 2.0
URL:		https://github.com/%{upstream}/erlang_%{realname}
VCS:		scm:git:https://github.com/%{upstream}/erlang_%{realname}.git
Source0:	https://github.com/%{upstream}/erlang_%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
Source1:	erlang-protobuffs-protoc-erl
BuildRequires:	erlang-meck
# It seems that PropEr support was broken for a very long time. See this PR for
# further details - https://github.com/basho/erlang_protobuffs/issues/100
#BuildRequires:	erlang-proper
BuildRequires:	erlang-meck
BuildRequires:	erlang-rebar


%description
A set of Protocol Buffers tools and modules for Erlang applications.


%prep
%autosetup -p1 -n erlang_%{realname}-%{version}


%build
%{erlang_compile}


%install
%{erlang_install}
# Install Erlang protobuf compiler script
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/protoc-erl


%check
%{erlang_test}


%files
%license LICENSE
%doc AUTHORS CONTRIBUTING.md README.md README_ORIG.md RELNOTES.md
%{_bindir}/protoc-erl
%{erlang_appdir}/


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.9.1-4
- Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 14 2018 Peter Lemenkov <lemenkov@gmail.com> - 0.9.1-1
- Ver. 0.9.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 29 2016 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.9.0-1
- Ver. 0.9.0

* Tue May 24 2016 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.3-1
- Ver. 0.8.3

* Wed Apr 27 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-2
- Spec-file cleanups

* Wed Mar  2 2016 Peter Lemenkov <lemenkov@gmail.com> - 0.8.2-1
- Ver. 0.8.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Sep 01 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-3
- Fixed FTBFS by adding workaround for rebar-related issue #960079

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 03 2013 Peter Lemenkov <lemenkov@gmail.com> - 0.8.0-1
- Ver. 0.8.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Sep 05 2012 Peter Lemenkov <lemenkov@gmail.com> - 0.7.0-1
- Upstream is switched to Basho
- Ver. 0.7.0
- Dropped all Basho's patches

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.20100930git58ff962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20100930git58ff962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Mar 11 2011 Peter Lemenkov <lemenkov@gmail.com> -  0-0.4.20100930git58ff962
- Added three patches from Basho's fork (required for riak_client)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20100930git58ff962
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct  5 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.2.20100930git58ff962
- Fixed License tag

* Thu Sep 30 2010 Peter Lemenkov <lemenkov@gmail.com> - 0-0.1.20100930git58ff962
- Initial package
