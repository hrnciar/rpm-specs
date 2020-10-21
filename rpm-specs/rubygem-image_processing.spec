# Generated from image_processing-1.11.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name image_processing

# ruby-vips gem is not in Fedora yet
%bcond_with vips

Name: rubygem-%{gem_name}
Version: 1.11.0
Release: 1%{?dist}
Summary: High-level wrapper for processing images for the web with ImageMagick or libvips
License: MIT
URL: https://github.com/janko/image_processing
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Tests are not shipped with the gem, you may check them out like so:
# git clone --no-checkout https://github.com/janko/image_processing
# cd image_processing && git archive -v -o image_processing-1.11.0-tests.txz v1.11.0 test/
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(minitest) >= 5.8
BuildRequires: rubygem(mini_magick)
%if %{with vips}
BuildRequires: rubygem(ruby-vips)
%endif
BuildArch: noarch

%description
High-level wrapper for processing images for the web with ImageMagick or
libvips.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1

# ruby-vips is not in Fedora yet. ImageMagick can be used instead.
%if %{without vips}
%gemspec_remove_dep -g ruby-vips
%endif

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .

# Tests dependencies that are not needed
sed -i '/require .minitest.hooks/ s/^/#/g' test/test_helper.rb
sed -i '/require .minispec-metadata/ s/^/#/g' test/test_helper.rb
sed -i '/require .bundler./ s/^/#/g' test/test_helper.rb

# vips gem is not in Fedora yet
%if %{without vips}
sed -i '/require .vips./ s/^/#/g' test/test_helper.rb
sed -i '/require .image_processing.vips./ s/^/#/g' test/pipeline_test.rb
mv test/vips_test.rb{,.disable}
sed -i '/::Vips/ i \  skip' test/pipeline_test.rb
sed -i '/Vips::/ i \  skip' test/test_helper.rb
%endif

# Use the RUBY_ENGINE check to avoid phashion dependency
sed -i '/RUBY_ENGINE == "jruby"/ s/jruby/ruby/' test/test_helper.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.txt
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Tue Aug 11 2020 Pavel Valena <pvalena@redhat.com> - 1.11.0-1
- Initial package
  Resolves: rhbz#1869719
