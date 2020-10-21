# Generated from railties-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name railties

# Circular dependency with rubygem-{rails,jquery-rails,uglifier}.
%bcond_with bootstrap

# `webpacker` dependency is required for a lot of tests, however it is not
# in Fedora yet
%bcond_with webpacker

Name: rubygem-%{gem_name}
Version: 6.0.3.4
Release: 1%{?dist}
Summary: Tools for creating, working with, and running Rails applications
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# Get the test suite:
# git clone http://github.com/rails/rails.git
# cd rails/railties && git archive -v -o railties-6.0.3.4-tests.txz v6.0.3.4 test/
Source1: %{gem_name}-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-6.0.3.4-tools.txz v6.0.3.4 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz

# dbconsole requires the executable.
Suggests: %{_bindir}/sqlite3
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
%if %{without bootstrap}
BuildRequires: rubygem(actioncable) = %{version}
BuildRequires: rubygem(actionmailer) = %{version}
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(activerecord) = %{version}
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activestorage) = %{version}
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(method_source)
BuildRequires: rubygem(rake) >= 0.8.7
BuildRequires: rubygem(rack-cache)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(bootsnap)
BuildRequires: rubygem(capybara)
#BuildRequires: rubygem(pg)
#BuildRequires: postgresql
BuildRequires: %{_bindir}/sqlite3
BuildRequires: rubygem(sprockets-rails)
BuildRequires: rubygem(thor) >= 0.18.1
# Needed `reline` for irb
BuildRequires: ruby-default-gems
BuildRequires: rubygem(turbolinks)
BuildRequires: %{_bindir}/git
BuildRequires: rubygem(jquery-rails)
BuildRequires: rubygem(uglifier)
BuildRequires: rubygem(rails)
BuildRequires: %{_bindir}/node
%if %{with webpacker}
BuildRequires: %{_bindir}/webpacker
%endif
%endif
BuildArch: noarch

%description
Rails internals: application bootup, plugins, generators, and rake tasks.
Railties is responsible to glue all frameworks together. Overall, it:
* handles all the bootstrapping process for a Rails application;
* manages rails command line interface;
* provides Rails generators core;

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -p .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%if %{without bootstrap}
%check
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}%{?prerelease}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s %{gem_dir}/gems/activesupport-%{version}%{?prerelease}/ .%{gem_dir}/gems/activesupport
ln -s %{gem_dir}/gems/activestorage-%{version}%{?prerelease}/ .%{gem_dir}/gems/activestorage
ln -s %{gem_dir}/gems/actionmailer-%{version}%{?prerelease}/ .%{gem_dir}/gems/actionmailer
ln -s %{gem_dir}/gems/activerecord-%{version}%{?prerelease}/ .%{gem_dir}/gems/activerecord
ln -s %{gem_dir}/gems/actionview-%{version}%{?prerelease}/ .%{gem_dir}/gems/actionview
ln -s %{gem_dir}/gems/actioncable-%{version}%{?prerelease}/ .%{gem_dir}/gems/actioncable
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/railties

# tmp dir has to exist for tests
mkdir -p .%{gem_dir}/gems/tmp/templates/app_template

pushd .%{gem_dir}/gems/railties

ln -s %{_builddir}/tools ..
mv %{_builddir}/test .

# Expected by InfoTest#test_rails_version
echo '%{version}%{?prerelease}' > ../RAILS_VERSION

touch ../Gemfile
echo 'gem "actioncable"' >> ../Gemfile
echo 'gem "actionmailer"' >> ../Gemfile
echo 'gem "actionpack"' >> ../Gemfile
echo 'gem "activerecord"' >> ../Gemfile
echo 'gem "activesupport"' >> ../Gemfile
echo 'gem "activestorage"' >> ../Gemfile
echo 'gem "method_source"' >> ../Gemfile
echo 'gem "rack-test"' >> ../Gemfile
echo 'gem "rack-cache"' >> ../Gemfile
echo 'gem "rake"' >> ../Gemfile
echo 'gem "rdoc"' >> ../Gemfile
echo 'gem "sqlite3"' >> ../Gemfile
echo 'gem "thor"' >> ../Gemfile
echo 'gem "turbolinks"' >> ../Gemfile
echo 'gem "sprockets-rails"' >> ../Gemfile
echo 'gem "puma"' >> ../Gemfile
echo 'gem "bootsnap"' >> ../Gemfile
echo 'gem "capybara"' >> ../Gemfile
echo 'gem "irb"' >> ../Gemfile
#echo 'gem "pg"' >> ../Gemfile
echo 'gem "jquery-rails"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "uglifier", require: false' >> ../Gemfile

# TODO: autorequires 'capybara/dsl' fail, not sure how to fix this.
sed -i '/def test_system_tests_are_run_through_rake_test_when_given_in_TEST$/,/^    end$/ s/^/#/' \
  test/application/test_runner_test.rb
sed -i '/def test_reset_sessions_before_rollback_on_system_tests$/,/^    end$/ s/^/#/' \
  test/application/test_runner_test.rb

# This works only when AR is not specified in Gemfile. Not sure how to
# workaround this.
sed -i '/test "database middleware doesn.t initialize when activerecord is not in frameworks" do$/,/^    end$/ s/^/#/' \
  test/application/initializers/frameworks_test.rb

# Requires running PostgreSQL server
mv test/application/rake/dbs_test.rb{,.disable}

# TODO: Mismatch in RAILS_FRAMEWORK_ROOT, not sure how to fix it.
sed -i '/test "i18n files have lower priority than application ones" do$/,/^    end$/ s/^/#/' \
  test/railties/engine_test.rb

# Disable unstable test.
# https://github.com/rails/rails/issues/25774
#sed -i '/^  def test_sqlite3_db_without_defined_rails_root$/,/^  end$/ s/^/#/' test/commands/dbconsole_test.rb

# Plugin for minitest results in inconsistent behavior across various methods of test execution.
# https://github.com/rails/rails/issues/29899#issuecomment-321954028
#sed -i '/def test_output_inline_by_default$/,/^  end$/ s/^/#/' \
#  test/generators/plugin_test_runner_test.rb

# Requires running PostgreSQL server
#mv test/commands/dbconsole_test.rb{,.disable}

# Remove unneded dependency minitest/retry
sed -i -e '/require..minitest.retry./ s/^/#/' \
  test/isolation/abstract_unit.rb

export RUBYOPT="-I${PWD}/../railties/lib"
export PATH="${PWD}/../railties/exe:$PATH"

# Needed for test/generators/test_runner_in_engine_test.rb and
# test/generators/plugin_generator_test.rb
export BUNDLE_GEMFILE=${PWD}/../Gemfile

# Start PostgreSQL server
#PG_DIR=$(mktemp -d)
#export PGHOST=localhost
#postgres -D $PG_DIR -p 5432 &>/dev/null &
#mPID=$!

# yarn requires network access
sed -i -e '/^\s*sh .yarn/ s/^/#/g' \
  test/isolation/abstract_unit.rb

# All these tests bellow try to run `webpacker`
%if %{without webpacker}
sed -i -e '/^\s*sh .bin.rails webpacker/ s/^/#/g' \
  test/isolation/abstract_unit.rb

mv -v test/app_loader_test.rb{,.disable}
mv -v test/engine/test_test.rb{,.disable}
mv -v test/secrets_test.rb{,.disable}

for tname in \
  railtie \
  engine \
  mounted_engine \
;do
  mv -v test/railties/${tname}_test.rb{,.disable}
done

for tname in \
  credentials \
  encrypted \
  initializers \
  notes \
  routes \
  secrets \
  server \
;do
  mv -v test/commands/${tname}_test.rb{,.disable}
done
rm -rf test/application/

sed -i '/^\s*def test_ensure_that_migration_tasks_work_with_mountable_option/ a \  skip' \
  test/generators/plugin_generator_test.rb

sed -i -e '/^\s*def test_scaffold_tests_pass_by_default_inside_mountable_engine/ a \  skip' \
       -e '/^\s*def test_scaffold_tests_pass_by_default_inside_namespaced_mountable_engine/ a \  skip' \
       -e '/^\s*def test_scaffold_tests_pass_by_default_inside_full_engine/ a \  skip' \
       -e '/^\s*def test_scaffold_tests_pass_by_default_inside_api_full_engine/ a \  skip' \
       -e '/^\s*def test_scaffold_tests_pass_by_default_inside_api_mountable_engine/ a \  skip' \
  test/generators/scaffold_generator_test.rb
%endif

# The reporting syntax seems to have changed. The test will be fixed in 6.0.4.
# https://github.com/rails/rails/issues/40081
sed -i -e '/^\s*test "outputs errors inline" do/ a \  skip' \
       -e '/^\s*test "outputs colored failed results" do/ a \  skip' \
  test/test_unit/reporter_test.rb

# Uses `Bundler.stub`
sed -i '/^\s*def test_generation_use_original_bundle_environment/ a \  skip' \
  test/generators/app_generator_test.rb

# Not sure why this fails,
# https://github.com/rails/rails/issues/40081
sed -i -e '/^\s*test "outputs colored failed results" do/ a \  skip' \
       -e '/^\s*test "outputs errors inline" do/ a \  skip' \
  test/test_unit/reporter_test.rb

# Tests needs to be executed in isolation.
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Itest -- '{}' || exit 255"

#kill -9 $mPID
popd
%endif

%files
%dir %{gem_instdir}
%{_bindir}/rails
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/RDOC_MAIN.rdoc
%doc %{gem_instdir}/README.rdoc

%changelog
* Thu Oct  8 11:34:50 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.4-1
- Update to railties 6.0.3.4.
  Resolves: rhbz#1877509

* Tue Sep 22 00:33:17 CEST 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.3-1
- Update to railties 6.0.3.3.
  Resolves: rhbz#1877509

* Mon Aug 17 05:27:18 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.2-1
- Update to railties 6.0.3.2.
  Resolves: rhbz#1742801

* Tue Aug 04 16:14:56 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to Railties 6.0.3.1.
  Resolves: rhbz#1742801

* Mon Aug 03 2020 Vít Ondruch <vondruch@redhat.com> - 5.2.3-6
- Fix test failure due to Ruby 2.7 and Puma 4.2.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-6
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-2
- Enable tests.

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Railties 5.2.3.

* Mon Mar 18 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-2
- Enable tests.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Railties 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-2
- Update to Railties 5.2.2.

* Thu Aug 09 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-2
- Enable tests.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Railties 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-2
- Enable tests.

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Railties 5.2.0.

* Mon Feb 19 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-2
- Enable tests.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-1
- Update to Railties 5.1.5.
  Removed patch{6,7,8}; subsumed

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Vít Ondruch <vondruch@redhat.com> - 5.1.4-3
- Fix Minitest 5.11 compatibility.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-2
- Enable tests.

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-1
- Update to Railties 5.1.4.

* Sat Aug 12 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-2
- Enable tests.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-1
- Update to Railties 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-2
- Enable tests.

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-1
- Update to Railties 5.1.2.

* Mon Jun 26 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-2
- Enable tests.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-1
- Update to Railties 5.1.1.
  - git support with tests
  - puma dependent tests

* Sat May 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 5.0.2-3
- Patch for minitest 5.10.2 compatibility (rhbz 1449430)

* Tue Mar 07 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-2
- Enable tests.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-1
- Update to Railties 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Vít Ondruch <vondruch@redhat.com> - 5.0.1-2
- Fix Listen 3.1.x compatibility.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-1
- Update to Railties 5.0.1.
- Remove Patch0 and Patch1: rubygem-railties-5.0.0-Do-not-run-bundle-install-when-generating-a-new-plugin{,-test}.patch; subsumed

* Wed Aug 17 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0.1-2
- Enable whole test suite.

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-1
- Update to Railties 5.0.0.1

* Tue Jul 12 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0-1
- Update to Railties 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 4.2.6-1
- Update to railties 4.2.6

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.2-1
- Update to railties 4.2.5.2

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 4.2.5.1-1
- Update to railties 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 4.2.5-1
- Update to railties 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 4.2.4-1
- Update to railties 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 4.2.3-1
- Update to railties 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 4.2.2-1
- Update to railties 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 4.2.1-1
- Update to railties 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 4.2.0-1
- Update to railties 4.2.0
- Disable tests for now, they are too unstable

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to railties 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to railties 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 4.1.1-1
- Update to Railties 4.1.1

* Wed Apr 23 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Apr 15 2014 Josef Stribny <jstribny@redhat.com> - 4.1.0-1
- Update to Railties 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 4.0.3-1
- Update to Railties 4.0.3

* Wed Feb 05 2014 Josef Stribny <jstribny@redhat.com> - 4.0.2-2
- Fix license (SyntaxHighlighter is removed in 4.x.x)

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 4.0.2-1
- Update to Railties 4.0.2

* Thu Nov 14 2013 Josef Stribny <jstribny@redhat.com> - 4.0.1-1
- Update to Railties 4.0.1.

* Thu Aug 08 2013 Josef Stribny <jstribny@redhat.com> - 4.0.0-1
- Update to Railties 4.0.0.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 11 2013 Josef Stribny <jstribny@redhat.com> - 3.2.13-1
- Fix license.

* Sat Mar 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-3
- Relax RDoc dependency.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.12-1
- Update to Railties 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.11-1
- Update to Railties 3.2.11.

* Fri Jan 04 2013 Vít Ondruch <vondruch@redhat.com> - 3.2.10-1
- Update to Railties 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.8-1
- Update to Railties 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 3.2.7-1
- Update to Railties 3.2.7.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.2.6-1
- Update to Railties 3.2.6.
- Move some files into -doc subpackage.
- Remove the unneeded %%defattr.
- Introduce %%check section (not running tests yet, as they are part of dependency loop).

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.15-1
- Update to Railties 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 3.0.13-1
- Update to Railties 3.0.13.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to Railties 3.0.11.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.10-1
- Update to Railties 3.0.10

* Thu Jul 21 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-2
- Added missing RDoc dependency.

* Thu Jul 07 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.9-1
- Update to Railties 3.0.9

* Mon Jun 27 2011  <mmorsi@redhat.com> - 3.0.5-2
- include fix for BZ #715385

* Tue Mar 29 2011 Vít Ondruch <vondruch@redhat.com> - 3.0.5-1
- Updated to Railties 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011  <Minnikhanov@gmail.com> - 3.0.3-7
- Fix Comment 11 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c11
- Take LICENSE file from upstream.

* Mon Jan 31 2011  <Minnikhanov@gmail.com> - 3.0.3-6
- Fix Comment 9 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c9
- Temporarily test suite is blocked.

* Thu Jan 27 2011  <Minnikhanov@gmail.com> - 3.0.3-5
- Fix Comment 7 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c7 

* Tue Jan 25 2011  <Minnikhanov@gmail.com> - 3.0.3-4
- Fix Comment 5 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c5 

* Mon Jan 24 2011  <Minnikhanov@gmail.com> - 3.0.3-3
- Fix Comment 3 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c3 

* Sun Jan 23 2011  <Minnikhanov@gmail.com> - 3.0.3-2
- Fix Comment 1 #665560. https://bugzilla.redhat.com/show_bug.cgi?id=668090#c1 

* Fri Jan 07 2011  <Minnikhanov@gmail.com> - 3.0.3-1
- Initial package

