%global gem_name redis

Name: rubygem-%{gem_name}
Version: 4.2.2
Release: 1%{?dist}
Summary: A Ruby client library for Redis
License: MIT
URL: https://github.com/redis/redis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/redis/redis-rb.git && cd redis-rb
# git archive -v -o redis-rb-4.2.2-tests.txz v4.2.2 makefile test/ bin/
Source1: %{gem_name}-rb-%{version}-tests.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(hiredis)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildRequires: %{_bindir}/redis-server
BuildArch: noarch

%description
A Ruby client that tries to match Redis' API one-to-one, while still
providing an idiomatic interface.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}

cp -a %{_builddir}/{makefile,test} .

# Do not use bundler & rake for tests execution
sed -i "s/bundle exec rake test/ruby -Ilib:test -e \"Dir.glob('.\/test\/**\/*_test.rb').sort.each {|t| require t}\"/" \
  makefile

# We are using packaged Redis, so provide just dummy Redis build script.
mkdir bin
echo '#!/usr/bin/sh' > bin/build
chmod a+x bin/build

# copy cluster_creator from actual bin/
# (uses require_relative; thus `ln` not possible)
mv %{_builddir}/bin/cluster_creator bin/

# Set locale because two tests fail in mock.
# https://github.com/redis/redis-rb/issues/345
LANG=C.UTF-8

# Test ruby and hiredis drivers
for driver in ruby hiredis ; do
export DRIVER=$driver
make BINARY=$(which redis-server) REDIS_CLIENT=$(which redis-cli) BUILD_DIR='${TMP}'
# Give some time for Redis shutdown.
sleep 1
done
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Sep 10 2020 Vít Ondruch <vondruch@redhat.com> - 4.2.2-1
- Update to redis 4.2.2.
  Resolves: rhbz#1846288
  Resolves: rhbz#1863730

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Pavel Valena <pvalena@redhat.com> - 4.1.3-1
- Update to redis-rb 4.1.3.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Vít Ondruch <vondruch@redhat.com> - 4.1.1-1
- Update to redis 4.1.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.0.1-3
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 4.0.1-1
- Update to redis 4.0.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 3.2.2-2
- Update for rpmlint check
- Remove tests

* Mon Feb 08 2016 Greg Hellings <greg.hellings@gmail.com> - 3.2.2-1
- New upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 15 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.2.1-1
- Update to 3.2.1 (RHBZ #1192389)
- Remove Fedora 19 compatibility macros
- Use static test.conf, since upstream uses a dynamic ERB template now
- Correct comment about IPv6 support

* Mon Dec 15 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.2.0-1
- Update to 3.2.0 (RHBZ #1173070)
- Drop unneeded BRs
- Use %%license macro
- Adjustments for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Unconditionally pass tests for now (RHBZ #1173070)

* Mon Jun 09 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 3.1.0-1
- Update to 3.1.0
- Remove gem2rpm comment
- Patch for Minitest 5

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Feb 24 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 3.0.7-1
- Update to 3.0.7

* Tue Sep 03 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-3
- Move %%exclude .gitignore to -doc
- Reference to redis related bug

* Thu Jun 27 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-2
- Fix failing test
- Remove redis from Requires
- Exclude dot file

* Sun Jun 23 2013 Axilleas Pipinellis <axilleaspi@ymail.com> - 3.0.4-1
- Initial package
