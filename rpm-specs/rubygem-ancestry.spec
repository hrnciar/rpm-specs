%global gem_name ancestry

Name: rubygem-%{gem_name}
Version: 3.0.0
Release: 8%{?dist}
Summary: Organize ActiveRecord model into a tree structure
License: MIT
URL: http://github.com/stefankroes/ancestry
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

# For tests, which are not present in gem file
# git clone  https://github.com/stefankroes/ancestry.git && cd ancestry
# git checkout v3.0.0
# tar czvf rubygem-ancestry-3.0.0-test.tar.gz test/
Source1: %{name}-%{version}-test.tar.gz

BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(minitest)
BuildRequires: rubygems
BuildRequires: rubygem(sqlite3)

%description
Ancestry allows the records of a ActiveRecord model to be organized in a tree
structure, using a single, intuitively formatted database column. It exposes
all the standard tree structure relations (ancestors, parent, root, children,
siblings, descendants) and all of them can be fetched in a single sql query.
Additional features are named_scopes, integrity checking, integrity restoration,
arrangement of (sub)tree into hashes and different strategies for dealing with
orphaned records.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd ./%{gem_instdir}
tar zxf %{SOURCE1}
sed -i '/require.*bundler/d' test/environment.rb
mkdir log
touch log/test.log
cat <<EOF > test/database.yml
sqlite3:
  adapter: sqlite3
  database: ":memory:"
EOF
# Remove simplecov, coveralls, test/unit, debugger requirements
sed -i -e '3,10d' test/environment.rb
ruby -Ilib -Itest -rminitest/autorun -e "Dir.glob './test/**/*_test.rb', &method(:require)"
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE
%exclude %{gem_instdir}/init.rb
%exclude %{gem_instdir}/install.rb

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Dominic Cleal <dominic@cleal.org> - 3.0.0-1
- Update to 3.0.0

* Tue May 02 2017 Dominic Cleal <dominic@cleal.org> - 2.2.2-1
- Update to 2.2.2

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 31 2016 Jun Aruga <jaruga@redhat.com> - 2.1.0-4
- Fix test suite for Ruby 2.3 compatibility.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 16 2014 Josef Stribny <jstribny@redhat.com> - 2.1.0-1
- Update to 2.1.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.0-5
- enable test
- mark README and LICENSE as doc

* Tue Aug 13 2013 Miroslav Suchý <msuchy@redhat.com> 2.0.0-4
- fix typos 

* Tue Aug 13 2013 msuchy@redhat.com - 2.0.0-1
- Initial package
