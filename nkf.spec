%define	name         nkf
%define	version      2.07
%define	src_version  207b1
%define	release      %mkrel 0.2

Summary:   Network Kanji code conversion Filter
Name:      %{name}
Version:   %{version}
Release:   %{release}
License:   BSD-like
Group:     System/Internationalization
URL:       http://sourceforge.jp/projects/nkf/
Source:    http://prdownloads.sourceforge.jp/nkf/20055/%{name}%{src_version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Nkf is a yet another kanji code converter among networks, hosts and
terminals.  It converts input kanji code to designated kanji code such
as 7-bit JIS, MS-kanji (shifted-JIS) or EUC.

%prep
%setup -q -n %{name}207

%build
%make

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -s -m 755 nkf $RPM_BUILD_ROOT%{_bindir}

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 nkf.1 $RPM_BUILD_ROOT%{_mandir}/man1

install -d $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -m 644 nkf.1j $RPM_BUILD_ROOT%{_mandir}/ja/man1/nkf.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc nkf.doc
%{_bindir}/nkf
%{_mandir}/man1/nkf.1*
%{_mandir}/ja/man1/nkf.1*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.07-0.2mdv2010.0
+ Revision: 430174
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 2.07-0.1mdv2008.1
+ Revision: 136632
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - import nkf


* Mon May 15 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 2.07-0.1mdk
- new release (2.07-beta1)
- change URL

* Wed May 11 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.92-5mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.92-4mdk
- rebuild

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.92-3mdk
- rebuild

* Fri Oct 11 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.92-2mdk
- rebuild

* Fri Sep 14 2001 Renaud Chaillat <rchaillat@mandrakesoft.com> 1.92-1mdk
- first mandrake release

* Wed Feb 28 2001 SATO Satoru <ssato@redhat.com>
- nkf.copyright attached
- use system-defined macros (%%*dir)

* Tue Aug 29 2000 ISHIKAWA Mutsumi <ishikawa@redhat.com>
- adopt FHS

* Mon Aug  7 2000 ISHIKAWA Mutsumi <ishikawa@redhat.com>
- japanese manpages moved ja_JP.eucJP -> ja
- modified to be able to build by normal user.

* Tue Aug 01 2000 Yukihiro Nakai <ynakai@redhat.com>
- Update to 1.92
- rebuild for 7.0J

* Sat Mar 25 2000 Matt Wilson <msw@redhat.com>
- rebuilt for 6.2j
- support compressed man pages

* Wed Mar 22 2000 Chris Ding <cding@redhat.com>
- ja_JP.ujis -> ja_JP.eucJP

* Thu Oct  7 1999 Matt Wilson <msw@redhat.com>
- rebuilt against 6.1

* Sun May 30 1999 FURUSAWA,Kazuhisa <kazu@linux.or.jp>
- 1st Release for i386 (glibc2.1).
- Original Packager: Kazuhiko Mori(COW) <cow@he.mirai.ne.jp>

* Sun Jan 10 1999 Kazuhiko Mori(COW) <cow@he.mirai.ne.jp>
- just rebuilt for glibc TL. (release not changed.)

