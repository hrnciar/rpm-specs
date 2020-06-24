# Generated from web-console-2.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name web-console

%global rails_version 5.0.0

Name: rubygem-%{gem_name}
Version: 3.5.1
Release: 7%{?dist}
Summary: A debugging tool for your Ruby on Rails applications
License: MIT
URL: https://github.com/rails/web-console
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/web-console.git && cd web-console
# git checkout v3.5.1 && tar czvf web-console-3.5.1-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# The web-console 3.3.1 dropped support for RoR 4.2.
BuildRequires: rubygem(railties) >= %{rails_version}
BuildRequires: rubygem(activemodel) >= %{rails_version}
BuildRequires: rubygem(actionview) >= %{rails_version}
BuildRequires: rubygem(bindex)
BuildRequires: rubygem(mocha)

BuildArch: noarch

%description
A debugging tool for your Ruby on Rails applications.


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

# We don't care about code coverage.
sed -i '/[Ss]imple[Cc]ov/ s/^/#/' test/test_helper.rb
# We don't use Bundler.
sed -i '/^Bundler.require/ s/^/#/' test/dummy/config/application.rb

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.markdown
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 10 2017 Jun Aruga <jaruga@redhat.com> - 3.5.1-1
- Update to web-console 3.5.1.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jun Aruga <jaruga@redhat.com> - 3.4.0-1
- Update to web-console 3.4.0.

* Wed Jul 20 2016 Vít Ondruch <vondruch@redhat.com> - 3.3.1-1
- Update to web-console 3.3.1.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 22 2015 Vít Ondruch <vondruch@redhat.com> - 2.2.1-1
- Update to web-console 2.2.1.

* Fri Jun 19 2015 Vít Ondruch <vondruch@redhat.com> - 2.1.3-1
- Update to web-console 2.1.3.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 27 2015 Vít Ondruch <vondruch@redhat.com> - 2.0.0-1
- Initial package
