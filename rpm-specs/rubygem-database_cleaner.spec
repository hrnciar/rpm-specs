# Generated from database_cleaner-1.4.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name database_cleaner

Name: rubygem-%{gem_name}
Version: 1.7.0
Release: 3%{?dist}
Summary: Strategies for cleaning databases
License: MIT
URL: http://github.com/DatabaseCleaner/database_cleaner
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: redis-test.conf
# git clone https://github.com/DatabaseCleaner/database_cleaner.git && cd database_cleaner
# git checkout v1.7.0 && tar czvf database_cleaner-1.7.0-tests.tar.gz spec/ examples/config/redis.yml
Source2: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/redis-server
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(redis)
BuildRequires: rubygem(rspec2)
BuildRequires: rubygem(sequel)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
Strategies for cleaning databases. Can be used to ensure a clean state for
testing.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 2

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
for l in spec features examples; do
ln -s %{_builddir}/$l $l
done

# Bundler just complicates everything in our case, remove it.
sed -i '/require "bundler"/ s/^/#/' spec/spec_helper.rb
sed -i '/Bundler.setup/ s/^/#/' spec/spec_helper.rb

# Some tests fail due to changes in AR 4.0.
# https://github.com/bmabey/database_cleaner/issues/237
sed -i '/\.should_receive(:increment_open_transactions)/{s/^/#/}' spec/database_cleaner/active_record/transaction_spec.rb
sed -i '/\.should_receive(:decrement_open_transactions)/{s/^/#/}' spec/database_cleaner/active_record/transaction_spec.rb

mkdir db
cat > db/config.yml << EOF
sqlite3:
  adapter: sqlite3
  database: db/test.sqlite3
  pool: 5
  timeout: 5000
EOF

# Disable MySql and Postgres ActiveRecord adapters for now. They need more
# configuration probably.
sed -i '/active_record\/connection_adapters\/mysql/{s/^/#/}' spec/database_cleaner/active_record/truncation_spec.rb
sed -i '/active_record\/connection_adapters\/post/{s/^/#/}' spec/database_cleaner/active_record/truncation_spec.rb
sed -i 's/\[ MysqlAdapter, Mysql2Adapter, SQLite3Adapter, PostgreSQLAdapter ]/\[SQLite3Adapter\]/' \
  spec/database_cleaner/active_record/truncation_spec.rb

# Disable MySql and Postgres for Sequel.
sed -r -i '/postgres|mysql2?:\/\/\// s/^/#/' spec/database_cleaner/sequel/{deletion,truncation}_spec.rb

# Start a testing Redis server instance
redis-server %{SOURCE1}

rspec2 \
  spec/database_cleaner/configuration_spec.rb \
  spec/database_cleaner/null_strategy_spec.rb \
  spec/database_cleaner/safeguard_spec.rb \
  spec/database_cleaner/active_record/*_spec.rb \
  spec/database_cleaner/active_record/truncation/sqlite3_spec.rb \
  spec/database_cleaner/generic \
  spec/database_cleaner/redis \
  spec/database_cleaner/sequel \

# Quite Redis server.
kill -INT `cat db/redis.pid`

popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/*.yml
%{gem_instdir}/Gemfile.lock
%doc %{gem_instdir}/CONTRIBUTE.markdown
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/History.rdoc
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 11 2019 Vít Ondruch <vondruch@redhat.com> - 1.7.0-1
- Update to Database Cleaner 1.7.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 15 2017 Vít Ondruch <vondruch@redhat.com> - 1.6.1-1
- Update to Database Cleaner 1.6.1.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 Vít Ondruch <vondruch@redhat.com> - 1.5.3-1
- Update to Database Cleaner 1.5.3.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Vít Ondruch <vondruch@redhat.com> - 1.4.1-1
- Update to database_cleaner 1.4.1.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Vít Ondruch <vondruch@redhat.com> - 1.1.1-1
- Update to database_cleaner 1.1.1.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.6.6-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 0.6.6-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 01 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.6-2
- Fixed -doc subpackage dependency.

* Mon Mar 21 2011 Vít Ondruch <vondruch@redhat.com> - 0.6.6-1
- Updated upstream version.

* Mon Mar 21 2011 Vít Ondruch <vondruch@redhat.com> - 0.5.2-2
- Added tests.

* Wed Oct 06 2010 Jozef Zigmund <jzigmund@redhat.com> - 0.5.2-1
- Initial package
