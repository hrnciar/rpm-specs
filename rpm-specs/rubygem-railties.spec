# Generated from railties-3.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name railties

# Circular dependency with rubygem-{rails,jquery-rails,uglifier}.
%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 5.2.3
Release: 4%{?dist}
Summary: Tools for creating, working with, and running Rails applications
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Get the test suite:
# git clone http://github.com/rails/rails.git && cd rails/railties/
# git checkout v5.2.3 && tar czvf railties-5.2.3-tests.tgz test/
Source1: railties-%{version}-tests.tgz

# Check value of result.source_location in
# test_unit/reporter.rb#format_rerun_snippet
# https://github.com/rails/rails/pull/32297
Patch6: rubygem-railties-5.1.5-check-value-of-result-source-location.patch

# dbconsole requires the executable.
Suggests: %{_bindir}/sqlite3
# Let's keep Requires and BuildRequires sorted alphabeticaly
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
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
BuildRequires: rubygem(turbolinks)
BuildRequires: %{_bindir}/git
%if ! 0%{?bootstrap}
BuildRequires: rubygem(jquery-rails)
BuildRequires: rubygem(uglifier)
BuildRequires: rubygem(rails)
BuildRequires: %{_bindir}/node
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
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch6 -p2
popd

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -p .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

%check
# fake RAILS_FRAMEWORK_ROOT
ln -s %{gem_dir}/specifications/rails-%{version}.gemspec .%{gem_dir}/gems/rails.gemspec
ln -s %{gem_dir}/gems/activesupport-%{version}/ .%{gem_dir}/gems/activesupport
ln -s %{gem_dir}/gems/activestorage-%{version}/ .%{gem_dir}/gems/activestorage
ln -s %{gem_dir}/gems/actionmailer-%{version}/ .%{gem_dir}/gems/actionmailer
ln -s %{gem_dir}/gems/activerecord-%{version}/ .%{gem_dir}/gems/activerecord
ln -s %{gem_dir}/gems/actionview-%{version}/ .%{gem_dir}/gems/actionview
ln -s %{gem_dir}/gems/actioncable-%{version}/ .%{gem_dir}/gems/actioncable
ln -s ${PWD}%{gem_instdir} .%{gem_dir}/gems/railties

pushd .%{gem_dir}/gems/railties

# Extract tests.
tar xzf %{SOURCE1}

# Expected by InfoTest#test_rails_version
echo '%{version}' > ../RAILS_VERSION

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
%if ! 0%{?bootstrap}
echo 'gem "jquery-rails"' >> ../Gemfile
echo 'gem "rails"' >> ../Gemfile
echo 'gem "uglifier", require: false' >> ../Gemfile
%else
# Depends on jquer-rails and uglifier.
mv test/application/assets_test.rb{,.disable}
mv test/application/asset_debugging_test.rb{,.disable}

sed -i '/def test_scaffold_.*tests_pass_by_default$/,/^    end$/ s/^/#/' test/application/rake_test.rb
sed -i '/def test_rake_routes_with_rake_options$/,/^    end$/ s/^/#/' test/application/rake_test.rb
sed -i '/def test_rails_routes_displays_message_when_no_routes_are_defined$/,/^    end$/ s/^/#/' test/application/rake_test.rb
sed -i '/def test_rails_routes_calls_the_route_inspector$/,/^    end$/ s/^/#/' test/application/rake_test.rb

sed -i '/def test_generated_controller_works_with_rails_test$/,/^    end$/ s/^/#/' test/application/test_runner_test.rb
sed -i '/def test_generated_scaffold_works_with_rails_test$/,/^    end$/ s/^/#/' test/application/test_runner_test.rb

# Depends on rails.
mv test/application/bin_setup_test.rb{,.disable}
mv test/test_unit/reporter_test.rb{,.disable}
mv test/application/configuration/custom_test.rb{,.disable}

sed -i '/def test_generation_runs_bundle_install_with_full_and_mountable$/,/^  end$/ s/^/#/' test/generators/plugin_generator_test.rb
sed -i '/def test_generate_application_.*_when_does_not_exist_in_mountable_engine$/,/^  end$/ s/^/#/' test/generators/plugin_generator_test.rb

sed -i '/def test_controller_tests_pass_by_default_inside_mountable_engine$/,/^  end$/ s/^/#/' test/generators/scaffold_controller_generator_test.rb
sed -i '/def test_controller_tests_pass_by_default_inside_full_engine$/,/^  end$/ s/^/#/' test/generators/scaffold_controller_generator_test.rb

sed -i '/def test_application_new_exits_with_message_and_non_zero_code_when_generating_inside_existing_rails_directory$/,/^  end$/ s/^/#/' test/generators/app_generator_test.rb
sed -i '/def test_application_new_show_help_message_inside_existing_rails_directory$/,/^  end$/ s/^/#/' test/generators/app_generator_test.rb
%endif

# Disable unstable test.
# https://github.com/rails/rails/issues/25774
sed -i '/^  def test_sqlite3_db_without_defined_rails_root$/,/^  end$/ s/^/#/' test/commands/dbconsole_test.rb

# This works only when AR is not specified in Gemfile. Not sure how to
# workaround this.
sed -i '/test "database middleware doesn.t initialize when activerecord is not in frameworks" do$/,/^    end$/ s/^/#/' \
  test/application/initializers/frameworks_test.rb

# TODO: Mismatch in RAILS_FRAMEWORK_ROOT, not sure how to fix it.
sed -i '/test "i18n files have lower priority than application ones" do$/,/^    end$/ s/^/#/' \
  test/railties/engine_test.rb

# TODO: autorequires 'capybara/dsl' fail, not sure how to fix this.
sed -i '/def test_system_tests_are_run_through_rake_test_when_given_in_TEST$/,/^    end$/ s/^/#/' \
  test/application/test_runner_test.rb
sed -i '/def test_reset_sessions_before_rollback_on_system_tests$/,/^    end$/ s/^/#/' \
  test/application/test_runner_test.rb

# Plugin for minitest results in inconsistent behavior across various methods of test execution.
# https://github.com/rails/rails/issues/29899#issuecomment-321954028
sed -i '/def test_output_inline_by_default$/,/^  end$/ s/^/#/' \
  test/generators/plugin_test_runner_test.rb

# Requires running PostgreSQL server
mv test/application/rake/dbs_test.rb{,.disable}
mv test/commands/dbconsole_test.rb{,.disable}

# Requires bootsnap
sed -i '/^  def test_new_application_load_defaults$/,/^  end$/ s/^/#/' \
  test/generators/app_generator_test.rb

# `secret_token` is deprecated; use secret_key_base instead
# https://github.com/rails/rails/commit/46ac5fe69a20d4539a15929fe48293e1809a26b0#diff-8be8dcaa57e7e4cfd216ccee36299525
sed -i 's/^\(\s*secrets\.secret_\)token/\1key_base/' \
  test/path_generation_test.rb

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

# Tests needs to be executed in isolation.
find test -type f -name '*_test.rb' -print0 | \
  sort -z | \
  xargs -0 -n1 -i sh -c "echo '* Test file: {}'; ruby -Itest -- '{}' || exit 255"

#kill -9 $mPID
popd

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

