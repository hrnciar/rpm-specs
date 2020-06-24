Name:          ckeditor
Version:       4.14.0
Release:       1%{?dist}
Summary:       WYSIWYG text editor to be used inside web pages

License:       GPLv2+ or LGPLv2+ or MPLv1.1
URL:           http://ckeditor.com/

Source0:       http://download.cksource.com/CKEditor/CKEditor/CKEditor%20%{version}/ckeditor_%{version}_standard.tar.gz

BuildArch:     noarch
BuildRequires: web-assets-devel

Requires:      web-assets-filesystem


%description
CKEditor is a text editor to be used inside web pages. It's a WYSIWYG editor,
which means that the text being edited on it looks as similar as possible to
the results users have when publishing it. It brings to the web common editing
features found on desktop editing applications like Microsoft Word and
OpenOffice.


%package samples
Summary:  Samples for %{name}
Requires: %{name} = %{version}-%{release}

%description samples
%{summary}.


%prep
%setup -qn %{name}

: Licenses
mkdir -p .rpm/{licenses,docs}
for LICENSE_FILE in $(find . -type f -name 'LICENSE*')
do
    DIR=$(dirname $LICENSE_FILE)
    mkdir -p .rpm/licenses/$DIR
    mv $LICENSE_FILE .rpm/licenses/$DIR/
done

: Docs
for DOC_FILE in $(find . -type f -name '*.md' -not -name 'LICENSE*')
do
    DIR=$(dirname $DOC_FILE)
    mkdir -p .rpm/docs/$DIR
    mv $DOC_FILE .rpm/docs/$DIR/
done

: wrong-file-end-of-line-encoding
find .rpm -type f -print0 | xargs -0 sed -i 's/\r$//'

: Delete bundled flash files
rm -rf samples/old/htmlwriter/{assets,outputforflash.html}


%build
# Empty build section, nothing to build


%install
mkdir -p %{buildroot}%{_webassetdir}/%{name}
cp -pr * %{buildroot}%{_webassetdir}/%{name}/

: Compat filesystem
mkdir -p %{buildroot}/%{_datadir}
ln -s %{_webassetdir}/%{name} %{buildroot}/%{_datadir}/%{name}


# https://fedoraproject.org/wiki/Packaging:Directory_Replacement#Scriptlet_to_replace_a_directory
%pretrans -p <lua>
path = "%{_datadir}/%{name}"
st = posix.stat(path)
if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
        suffix = 0
        while not status do
            suffix = suffix + 1
            status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
        end
        os.rename(path, path .. ".rpmmoved")
    end
end


%files
%{!?_licensedir:%global license %%doc}
%license .rpm/licenses/*
%doc .rpm/docs/*
%{_webassetdir}/%{name}
%{_datadir}/%{name}
%exclude %{_webassetdir}/%{name}/samples

%ghost %attr(644, root, root) %{_datadir}/%{name}.rpmmoved


%files samples
%{_webassetdir}/%{name}/samples


%changelog
* Fri Mar 20 2020 Shawn Iwinski <shawn@iwin.ski> - 4.14.0-1
- Update to 4.14.0 (RHBZ #1810020)
- CVE-2020-9281 (RHBZ #1814825,1814826,1814827)
- CVE-2020-9440

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Shawn Iwinski <shawn@iwin.ski> - 4.13.1-1
- Update to 4.13.1 (RHBZ #1724633)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 14 2019 Shawn Iwinski <shawn@iwin.ski> - 4.11.4-1
- Update to 4.11.4 (RHBZ #1683205)
- Fix rpmlint "W: invalid-license MPLv1.1+" by changing "MPLv1.1+" to "MPLv1.1"

* Sun Feb 24 2019 Shawn Iwinski <shawn@iwin.ski> - 4.11.2-2
- Fix EPEL6 build error (BUILDSTDERR: error: Explicit file attributes required
  in spec for: /builddir/build/BUILDROOT/ckeditor-4.11.2-1.el6.noarch/usr/share/ckeditor.rpmmoved)

* Sun Feb 24 2019 Shawn Iwinski <shawn@iwin.ski> - 4.11.2-1
- Update to 4.11.2 (RHBZ #1651703 / RHBZ #1651704 / RHBZ #1651705 / CVE-2018-17960)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 29 2018 Shawn Iwinski <shawn@iwin.ski> - 4.9.2-1
- Update to 4.9.2 (RHBZ #1556589)
- Fix license files

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 14 2017 Shawn Iwinski <shawn@iwin.ski> - 4.8.0-1
- Update to 4.8.0 (RHBZ #1525735)

* Sun Oct 08 2017 Shawn Iwinski <shawn@iwin.ski> - 4.7.3-1
- Update to 4.7.3 (RHBZ #1491261)

* Wed Aug 30 2017 Shawn Iwinski <shawn@iwin.ski> - 4.7.2-1
- Update to 4.7.2 (RHBZ #1482711)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Shawn Iwinski <shawn@iwin.ski> - 4.7.1-1
- Update to 4.7.1 (RHBZ #1455719)

* Mon Mar 06 2017 Shawn Iwinski <shawn@iwin.ski> - 4.6.2-1
- Update to 4.6.2 (RHBZ #1070102, RHBZ #1295348)
- CVE-2014-5191 (RHBZ #1139487)
- Update spec to use web assets packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 23 2014 Remi Collet <remi@fedoraproject.org> - 4.3.2-1
- Update to 4.3.2

* Thu Aug 15 2013 Orion Poplawski <orion@cora.nwra.com> 4.2-1
- Update to 4.2

* Thu Aug 15 2013 Orion Poplawski <orion@cora.nwra.com> 4.1-3
- Remove bundled flash code
- Move samples to sub-package

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Apr  7 2013 Remi Collet <remi@fedoraproject.org> - 4.1-1
- Update to 4.1
- provided ckeditor_basic.js for compatibility with 3.6
- don't provide default alias, #910590

* Tue Mar 19 2013 Orion Poplawski <orion@cora.nwra.com> 4.0.2-1
- Update to 4.0.2

* Tue Feb  5 2013 Remi Collet <remi@fedoraproject.org> - 3.6.6-1
- update to 3.6.6
- move _samples in doc
- don't package _source
- move php library to /usr/share/php
- fix httpd configuration (grant access) #894567

* Fri Sep 14 2012 Orion Poplawski <orion@cora.nwra.com> 3.6.4-1
- Update to 3.6.4

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 27 2012 Orion Poplawski <orion@cora.nwra.com> 3.6.3-1
- Update to 3.6.3

* Mon Jan 23 2012 Orion Poplawski <orion@cora.nwra.com> 3.6.2-2
- Make %%doc line explicit

* Tue Oct 25 2011 Orion Poplawski <orion@cora.nwra.com> 3.6.2-1
- Update to 3.6.2

* Wed Aug  3 2011 Orion Poplawski <orion@cora.nwra.com> 3.6.1-1
- Update to 3.6.1

* Wed Oct  6 2010 Orion Poplawski <orion@cora.nwra.com> 3.4.1-1
- Initial package
