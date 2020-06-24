# Generated from activemodel-serializers-xml-1.0.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activemodel-serializers-xml

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 9%{?dist}
Summary: XML serialization for Active Model objects and Active Record models
License: MIT
URL: http://github.com/rails/activemodel-serializers-xml
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/activemodel-serialization-xml
# cd activemodel-serialization-xml/
# git checkout v1.0.1 && tar czvf activemodel-serialization-xml-1.0.1-tests.tgz test/
Source1: activemodel-serialization-xml-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(activerecord)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(sqlite3)
BuildArch: noarch

%description
XML serialization for your Active Model objects and Active Record models -
extracted from Rails.


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
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/




# Run the test suite
%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# ActiveModel::TestCase was removed in Rails 5.1 (#27928).
# https://github.com/rails/activemodel-serializers-xml/pull/15
sed -i "s/ActiveModel::TestCase/ActiveSupport::TestCase/" test/active_model/xml_serialization_test.rb

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_instdir}/activemodel-serializers-xml.gemspec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Vít Ondruch <vondruch@redhat.com> - 1.0.1-3
- Fix test suite compatibility with Rails 5.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Vít Ondruch <vondruch@redhat.com> - 1.0.1-1
- Initial package
