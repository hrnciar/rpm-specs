# Generated from oauth-0.4.4.gem by gem2rpm -*- rpm-spec -*-
%global gem_name oauth

Name: rubygem-%{gem_name}
Version: 0.5.1
Release: 7%{?dist}
Summary: OAuth Core Ruby implementation
License: MIT
URL: https://github.com/oauth-xx/oauth-ruby
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# The keys are missing in test suite.
# https://github.com/oauth-xx/oauth-ruby/pull/142
Source1: https://raw.githubusercontent.com/oauth-xx/oauth-ruby/master/test/keys/rsa.cert
Source2: https://raw.githubusercontent.com/oauth-xx/oauth-ruby/master/test/keys/rsa.pem
# Fix WebMock compatibility.
# https://github.com/oauth-xx/oauth-ruby/issues/117
Patch0: rubygem-oauth-0.5.1-Adjusting-to-webmock-latest-recommended-implementation-for-minitest.patch
# Fix Rails 5.x compatibility
# https://github.com/oauth-xx/oauth-ruby/pull/134
Patch1: rubygem-oauth-0.5.1-Fix-ActionControllerRequestProxy-test-to-support-Rails-5.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(actionpack)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(webmock)
# Enable when available in Fedora.
# BuildRequires: rubygem(em-http-request)
BuildArch: noarch

%description
This is a RubyGem for implementing both OAuth clients and servers
in Ruby applications.

See the OAuth specs http://oauth.net/core/1.0/

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
%patch1 -p1
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# We don't need ByeBug.
sed -i "/'byebug'/ s/^/#/" test/test_helper.rb

# Restore keys needed by test suite.
# https://github.com/oauth-xx/oauth-ruby/pull/142
mkdir test/keys
cp %{SOURCE1} test/keys
cp %{SOURCE2} test/keys

ruby -Ilib -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/oauth
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/TODO
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Vít Ondruch <vondruch@redhat.com> - 0.5.1-1
- Update to OAuth 0.5.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Vít Ondruch <vondruch@redhat.com> - 0.4.7-7
- Update upstream URL.

* Tue Jun 17 2014 Vít Ondruch <vondruch@redhat.com> - 0.4.7-6
- Fix FTBFS in Rawhide (rhbz#1107182).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Vít Ondruch <vondruch@redhat.com> - 0.4.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Vít Ondruch <vondruch@redhat.com> - 0.4.7-1
- Update to OAuth 0.4.7.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Vít Ondruch <vondruch@redhat.com> - 0.4.4-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 15 2011 Vít Ondruch <vondruch@redhat.com> - 0.4.4-1
- Initial package
