Name:           jxrlib
Version:        1.1
Release:        14%{?dist}
Summary:        Open source implementation of jpegxr

# See JPEGXR_DPK_Spec_1.0.doc. Upstream request for plain text license file at
# https://jxrlib.codeplex.com/workitem/13
License:        BSD
URL:            https://jxrlib.codeplex.com/
Source0:        http://jxrlib.codeplex.com/downloads/get/685249#/jxrlib_%(echo %{version} | tr . _).tar.gz
# Use CMake to build to facilitate creation of shared libraries
# See https://jxrlib.codeplex.com/workitem/13
Source1:        CMakeLists.txt
# Converted from shipped doc/JPEGXR_DPK_Spec_1.doc
# libreoffice --headless --convert-to pdf doc/JPEGXR_DPK_Spec_1.0.doc
Source2:        JPEGXR_DPK_Spec_1.0.pdf

# Fix various warnings, upstreamable
# See https://jxrlib.codeplex.com/workitem/13
Patch0:         jxrlib_warnings.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  make


%description
This is an open source implementation of the jpegxr image format standard.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q -n %{name}

# Sanitize charset and line endings
for file in `find . -type f -name '*.c' -or -name '*.h' -or -name '*.txt'`; do
  iconv --from=ISO-8859-15 --to=UTF-8 $file > $file.new && \
  sed -i 's|\r||g' $file.new && \
  touch -r $file $file.new && mv $file.new $file
done

%patch0 -p1

# Remove shipped binaries
rm -rf bin

cp -a %{SOURCE1} .
cp -a %{SOURCE2} doc


%build
%cmake .
%make_build


%install
%make_install


%ldconfig_scriptlets


%files
%doc doc/readme.txt doc/JPEGXR_DPK_Spec_1.0.pdf
%{_bindir}/JxrEncApp
%{_bindir}/JxrDecApp
%{_libdir}/libjpegxr.so.*
%{_libdir}/libjxrglue.so.*

%files devel
%{_includedir}/jxrlib/
%{_libdir}/libjpegxr.so
%{_libdir}/libjxrglue.so


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 1.1-10
- Add missing BR: gcc, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Sandro Mani <manisandro@gmail.com> - 1.1-4
- Fix typo in jxrlib_warnings.patch

* Tue Sep 08 2015 Sandro Mani <manisandro@gmail.com> - 1.1-3
- Add Patch0 and Source1 upstream links
- Ship pdf variant of JPEGXR_DPK_Spec_1.0.doc in %%doc
- Remove bin folder

* Tue Sep 08 2015 Sandro Mani <manisandro@gmail.com> - 1.1-2
- Comments for Patch0 and Source1

* Wed Sep 02 2015 Sandro Mani <manisandro@gmail.com> - 1.1-1
- Initial package
