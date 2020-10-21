# Generated from guard-livereload-2.5.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name guard-livereload

Name: rubygem-%{gem_name}
Version: 2.5.2
Release: 8%{?dist}
Summary: Guard plugin for livereload
License: MIT
URL: https://rubygems.org/gems/guard-livereload
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(guard-compat)
BuildRequires: rubygem(em-websocket)
BuildRequires: rubygem(multi_json)
BuildArch: noarch

%description
Guard::LiveReload automatically reloads your browser when 'view' files are
modified.


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



%check
pushd .%{gem_instdir}

# We don't care about code coverage.
sed -i "/[Cc]overalls/ s/^/#/" spec/spec_helper.rb

CI=true rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/Guardfile
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/guard-livereload.gemspec
%{gem_instdir}/js
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 7 2020 Jaroslav Prokop <jar.prokop@volny.cz> - 2.5.2-7
- Revert commented out tests. Problem disappeared after update to Ruby 2.7.1-132.

* Wed Mar 4 2020 Jaroslav Prokop <jar.prokop@volny.cz> - 2.5.2-6
- Comment out tests failing on ruby 2.7.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jan 30 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 2.5.2-1
- Initial package
