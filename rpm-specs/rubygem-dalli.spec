%global gem_name dalli

# Depends on Rails and its needed by Rails
%global enable_test 0

Name: rubygem-%{gem_name}
Version: 2.7.8
Release: 5%{?dist}
Summary: High performance memcached client for Ruby
License: MIT
URL: https://github.com/petergoldstein/dalli
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/petergoldstein/dalli.git && cd dalli
# git checkout v2.7.8 && tar czvf dalli-2.7.8-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz

# Use 'assert_nil ...' instead of 'assert_equal nil, ...'
# https://github.com/petergoldstein/dalli/pull/661
Patch0: rubygem-dalli-2.7.6-Use-assert_nil-in-tests.patch
# Fix memcached 1.5.4 test compatibility.
# https://github.com/petergoldstein/dalli/pull/672
Patch1: rubygem-dalli-2.7.6-Fix-memcached-1.5.4-compatibility.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
%if 0%{enable_test} > 0
BuildRequires: memcached
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rails)
BuildRequires: rubygem(connection_pool)
%endif
BuildRequires: ruby
BuildArch: noarch

%description
High performance memcached client for Ruby


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
%if 0%{enable_test} > 0
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}
cat %{PATCH0} | patch -p1
cat %{PATCH1} | patch -p1
sed -i '/bundler/ s/^/#/' test/helper.rb
ruby -Ilib:test -e "Dir.glob('./test/test_*.rb').sort.each{ |x| require x }"
popd
%endif

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%license %{gem_instdir}/LICENSE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/History.md
%{gem_instdir}/Gemfile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Pavel Valena <pvalena@redhat.com> - 2.7.8-1
- Update to dalli 2.7.8.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Vít Ondruch <vondruch@redhat.com> - 2.7.6-4
- Fix memcached 1.5.4 test compatibility.

* Wed Aug 30 2017 Pavel Valena <pvalena@redhat.com> - 2.7.6-3
- Fix FTBFS(tests only) in rawhide.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 2.7.6-1
- Update to 2.7.6.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 18 2015 Josef Stribny <jstribny@redhat.com> - 2.7.4-1
- Update to 2.7.4

* Mon Jun 16 2014 Josef Stribny <jstribny@redhat.com> - 2.7.2-2
- Fix the test the right way

* Mon Jun 16 2014 Josef Stribny <jstribny@redhat.com> - 2.7.2-1
- Update to dalli 2.7.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 2.6.4-2
- Enable tests

* Wed Jul 31 2013 Josef Stribny <jstribny@redhat.com> - 2.6.4-1
- Initial package
