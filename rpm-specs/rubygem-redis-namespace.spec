%global gem_name redis-namespace

Name: rubygem-%{gem_name}
Version: 1.6.0
Release: 6%{?dist}
Summary: Namespaces Redis commands
License: MIT
URL: https://github.com/resque/redis-namespace
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: rubygem-redis-namespace-test.conf
# Method without arguments is outdated.
# https://github.com/resque/redis-namespace/commit/5806627
Patch0: rubygem-redis-namespace-1.6.0-fix-with-matcher-of-no-args.patch
# Fix tests with outdated fix-be_true be_false
# https://github.com/resque/redis-namespace/commit/ccc62f2
Patch1: rubygem-redis-namespace-1.6.0-fix-be_true-be_false.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# Use RSpec 3 instead RSpec2
# https://github.com/resque/redis-namespace/pull/155
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
BuildRequires: rubygem(redis)
BuildRequires: redis
BuildArch: noarch

%description
Adds a Redis::Namespace class which can be used to namespace calls
to Redis. This is useful when using a single instance of Redis with
multiple, different applications.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

cat "%{PATCH0}" | patch -p1
cat "%{PATCH1}" | patch -p1

# Remove dependency on bundler.
sed -i -e "/require 'bundler'/d" spec/spec_helper.rb
sed -i -e "/Bundler.setup/d" spec/spec_helper.rb
sed -i -e "/Bundler.require/d" spec/spec_helper.rb

# Redis server configuration
install -m 0644 %{SOURCE1} spec/test.conf
mkdir spec/db

# Start redis-server
redis-server spec/test.conf

rspec -r 'rspec/its' spec

# Kill redis-server
kill -INT "$(cat spec/db/redis.pid)"
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 20 2018 Jun Aruga <jaruga@redhat.com> - 1.6.0-2
- Remove jemalloc, as the issue was fixed.

* Fri Jun 15 2018 Jun Aruga <jaruga@redhat.com> - 1.6.0-1
- Update to 1.6.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 05 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.5.2-2
- Update to 1.5.2 (RHBZ #1207454)
- Drop Fedora 19 conditionals
- Patch for rspec 3 support
- Use %%license macro

* Thu Sep 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.5.1-1
- Update to 1.5.1 (RHBZ #1126616)

* Thu Jul 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.5.0-2
- Add missing gem source file

* Thu Jul 10 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.5.0-1
- Update to 1.5.0 (RHBZ #1114344)
- Avoid using the full path to redis-server during %%check, since this has
  changed in Fedora 21.

* Wed Jun 11 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.4.1-3
- Adjustments for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Bump the maximum redis version.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 04 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.4.1-1
- Update to 1.4.1 (RHBZ #1038151)
- Use HTTPS for URL

* Thu Nov 07 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.3.2-2
- Update to 1.3.2

* Sat Nov 02 2013 Ken Dreyer <ktdreyer@ktdreyer.com> - 1.3.1-1
- Initial package
