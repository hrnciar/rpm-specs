# Generated from mini_magick-4.8.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mini_magick

Name: rubygem-%{gem_name}
Version: 4.9.3
Release: 3%{?dist}
Summary: Manipulate images with minimal use of memory via ImageMagick
License: MIT
URL: https://github.com/minimagick/minimagick
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# The mini_magick gem doesn't ship with the test suite.
# You may check it out like so:
# git clone http://github.com/minimagick/minimagick.git && cd minimagick
# git checkout v4.9.3 && tar czvf mini_magick-4.9.3-tests.tgz spec/
Source1: %{gem_name}-%{version}-tests.tgz

Requires: ImageMagick
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
BuildRequires: ImageMagick
BuildArch: noarch

%description
A ruby wrapper for ImageMagick command line. Using MiniMagick the ruby
processes memory remains small (it spawns ImageMagick's command line program
mogrify which takes up some memory as well, but is much smaller compared
to RMagick).


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# Remove unneeded pry dependency.
# https://github.com/minimagick/minimagick/pull/453
# Also remove bundler.
sed -i -e '/require "pry"/ s/^/#/g' \
       -e '/require "bundler/ s/^/#/g' \
  spec/spec_helper.rb

# We do not use GraphicsMagic or posix-spawn
sed -i -e '/^  \[:imagemagick, :graphicsmagick\].each do |cli|$/ s/, :graphicsmagick//g' \
       -e '/^  \["open3", "posix-spawn"\].each do |shell_api|$/ s/, "posix-spawn"//g' \
  spec/spec_helper.rb
sed -i '/^    it "identifies when gm exists" do$/,/    end/ s/^/#/g' \
  spec/lib/mini_magick/utilities_spec.rb
sed -i "/^    it \"returns GraphicsMagick's version\" do$/,/    end/ s/^/#/g" \
  spec/lib/mini_magick_spec.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 27 2019 Pavel Valena <pvalena@redhat.com> - 4.9.3-1
- Update to mini_magick 4.9.3.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Pavel Valena <pvalena@redhat.com> - 4.8.0-1
- Initial package
